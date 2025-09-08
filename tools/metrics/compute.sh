#!/usr/bin/env bash
set -euo pipefail
GR="${GROVE_ROOT:-$([ -x ./tools/env/resolve_root.sh ] && ./tools/env/resolve_root.sh || pwd)}"
command -v jq >/dev/null 2>&1 || { echo "[metrics] jq required"; exit 2; }

grade_json="$GR/docs/status/handoff-grade.json"
index_json="$GR/docs/wfb/wfb.index.json"

pct_for() {
  case "$1" in
    [Bb]lue*)  echo 100;;
    [Gg]reen*) echo 85;;
    [Yy]ellow*)echo 60;;
    *)         echo 40;;
  esac
}
class_for() {
  case "$1" in
    [Bb]lue*)  echo blue;;
    [Gg]reen*) echo green;;
    [Yy]ellow*)echo yellow;;
    *)         echo red;;
  esac
}

# --- reuse ratio (rough, based on index markers)
reuse_count=$(grep -c 'reuse (' "$index_json" 2>/dev/null || true); reuse_count=${reuse_count:-0}
new_count=$(grep -c '\[new WFB\]' "$index_json" 2>/dev/null || true); new_count=${new_count:-0}
total=$(( reuse_count + new_count ))
if [ "$total" -gt 0 ]; then
  reuse_ratio=$(awk -v r="$reuse_count" -v t="$total" 'BEGIN{printf "%.3f", (t>0?r/t:0)}')
else
  reuse_ratio=0
fi

# --- problems freshness (hours since last VSCode problems file)
prob="$(ls -1t "$GR/docs/vscode"/problems-*.json 2>/dev/null | grep -v stub | head -n1 || true)"
if [ -n "${prob:-}" ] && [ -f "$prob" ]; then
  now=$(date +%s); mt=$(stat -c %Y "$prob"); fresh_hours=$(( (now-mt)/3600 ))
else
  fresh_hours=
fi

# --- DB detect (best-effort)
dbdet="$("$GR/tools/db/detect.sh" --machine 2>/dev/null || true)"
if echo "$dbdet" | grep -q 'engine='; then db="$(echo "$dbdet" | tr -d '\n')"; else db="unknown"; fi

# --- Crypto status (overall + detail lines)
crypto_report="$("$GR/tools/crypto/status.sh" 2>/dev/null || true)"
[ -n "${crypto_report:-}" ] || crypto_report="yellow: crypto probe missing"
crypto_overall="$(echo "$crypto_report" | head -n1)"
crypto_details="$(echo "$crypto_report" | tail -n +2 | sed 's/^ - //')"

# --- Key expiry (optional helper)
if [ -x "$GR/tools/crypto/key_expiry.sh" ]; then
  key_line="$("$GR/tools/crypto/key_expiry.sh" 2>/dev/null || true)"
else
  key_line="yellow: key expiry unknown"
fi

# --- Chats imported
imp_dir="$GR/docs/chats/imported"
if [ -d "$imp_dir" ]; then
  imp_cnt="$(find "$imp_dir" -type f 2>/dev/null | wc -l | tr -d ' ')"
  chats_status="green: imported ($imp_cnt files)"
else
  chats_status="yellow: none imported"
fi

# --- WFB scan presence
[ -f "$GR/docs/wfb/wfb.graph.json" ] && wfb_scan_status="green" || wfb_scan_status="yellow"

# --- Handoff grade (if present)
grade=$(jq -r '.grade // empty' "$grade_json" 2>/dev/null || true)
score=$(jq -r '.score // empty' "$grade_json" 2>/dev/null || true)

# --- Git basic health (legacy line)
git_status="$("$GR/tools/git/health.sh" 2>/dev/null || true)"; [ -n "${git_status:-}" ] || git_status="yellow: unknown"

# --- Build crypto detail rows
crypto_rows=""
while IFS= read -r line; do
  [ -z "$line" ] && continue
  bucket="$(printf '%s' "$line" | sed 's/^[^:]*:[[:space:]]*//')"   # text after "<status>: "
  cls=$(class_for "$line"); pct=$(pct_for "$line")
  crypto_rows="${crypto_rows}<div class=\"row sub\"><span class=\"label\">↳ ${bucket}</span><span class=\"badge ${cls}\" title=\"${line}\">${line}</span><span>${pct}%</span></div>"
done <<EOF
$crypto_details
EOF
# add key expiry line as a crypto sub-row
kcls=$(class_for "$key_line"); kpct=$(pct_for "$key_line")
crypto_rows="${crypto_rows}<div class=\"row sub\"><span class=\"label\">↳ key expiry</span><span class=\"badge ${kcls}\" title=\"${key_line}\">${key_line}</span><span>${kpct}%</span></div>"

# --- GitHub sub-rows from the probe
github_rows=""
if [ -x "$GR/tools/git/sync_report.sh" ]; then
  gh_lines="$("$GR/tools/git/sync_report.sh" 2>/dev/null || true)"
  # show each line as a sub-row
  while IFS= read -r g; do
    [ -z "$g" ] && continue
    gcls=$(class_for "$g"); gpct=$(pct_for "$g")
    label="$(printf '%s' "$g" | sed 's/^[^:]*:[[:space:]]*//')"
    github_rows="${github_rows}<div class=\"row sub\"><span class=\"label\">↳ ${label%% *}</span><span class=\"badge ${gcls}\" title=\"${g}\">${g}</span><span>${gpct}%</span></div>"
  done <<EOF
$gh_lines
EOF
else
  github_rows="<div class=\"row sub\"><span class=\"label\">↳ probe</span><span class=\"badge yellow\">yellow: sync probe not found</span><span>60%</span></div>"
fi

# --- Top-level gauges
git_pct=$(pct_for "$git_status")
cry_pct=$(pct_for "$crypto_overall")
ch_pct=$(pct_for "$chats_status")
wfb_pct=$(pct_for "$wfb_scan_status")

all_green=1
for k in "$git_status" "$crypto_overall" "$chats_status" "$wfb_scan_status"; do
  printf '%s' "$k" | grep -qi '^green' || all_green=0
done
overall_class=$([ "$all_green" = "1" ] && echo blue || echo green)
overall_pct=$([ "$all_green" = "1" ] && echo 100 || echo 85)

# --- HTML
mkdir -p "$GR/docs/status"
cat > "$GR/docs/status/index.html" <<HTML
<!doctype html><html><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Grove: Total System Performance</title>
<style>
:root { --fg:#0b1020; --bg:#f7f9fc; --card:#fff; --muted:#667; }
*{box-sizing:border-box} body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.5 ui-sans-serif,system-ui,Segoe UI,Roboto,Ubuntu}
.wrap{max-width:920px;margin:24px auto;padding:0 16px}
h1{margin:16px 0 8px} .muted{color:var(--muted)}
.card{background:var(--card);border-radius:14px;padding:16px 16px 8px;margin:12px 0;box-shadow:0 2px 10px rgba(0,0,0,.05)}
.grid{display:grid;grid-template-columns:1fr;gap:8px}
.badge{padding:2px 8px;border-radius:999px;font:12px ui-monospace,monospace;white-space:nowrap}
.green{background:#b2f5b2;color:#064}
.yellow{background:#ffe9a6;color:#7a5300}
.red{background:#ffc0c0;color:#600}
.blue{background:#cfe8ff;color:#063}
.row{display:grid;grid-template-columns: 280px 1fr 80px;gap:8px;align-items:center}
.row.sub{opacity:.95}
.row .label{font-weight:600}
a{color:#1149c9;text-decoration:none} a:hover{text-decoration:underline}
.small{font-size:12px}
</style>
</head><body><div class="wrap">
  <h1>Grove: Total System Performance</h1>
  <div class="muted">Grade: ${grade:-N/A} · Score: ${score:-N/A}</div>

  <div class="card">
    <div class="grid">
      <div class="row"><span class="label">System status (all checks)</span><span class="badge ${overall_class}">${overall_class}</span><span>${overall_pct}%</span></div>

      <div class="row"><span class="label">GitHub (local + connector readiness)</span><span class="badge $(class_for "$git_status")" title="${git_status}">${git_status}</span><span>${git_pct}%</span></div>
      ${github_rows}

      <div class="row"><span class="label">Crypto (sealed bundles)</span><span class="badge $(class_for "$crypto_overall")" title="${crypto_overall}">${crypto_overall}</span><span>${cry_pct}%</span></div>
      ${crypto_rows}

      <div class="row"><span class="label">Chats imported</span><span class="badge $(class_for "$chats_status")" title="${chats_status}">${chats_status}</span><span>${ch_pct}%</span></div>
      <div class="row"><span class="label">WFB scan</span><span class="badge $(class_for "$wfb_scan_status")" title="${wfb_scan_status}">${wfb_scan_status}</span><span>${wfb_pct}%</span></div>
    </div>
  </div>

  <div class="card">
    <div class="grid">
      <div class="row"><span class="label">Reuse ratio (reused/total)</span><span class="muted">${reuse_ratio}</span><span></span></div>
      <div class="row"><span class="label">Problems freshness (hours)</span><span class="muted">${fresh_hours:-N/A}</span><span></span></div>
      <div class="row"><span class="label">DB detect</span><span class="muted">${db}</span><span></span></div>
      <div class="row"><span class="label">Indexes & views</span>
        <span>
          <a href="../wfb/wfb.graph.json">raw graph</a> ·
          <a href="wfb-index.html">WFB index</a> · <a href="wfb-graph.html">WFB graph</a>
        </span><span></span>
      </div>
      <div class="row small"><span class="label">Legend</span>
        <span class="muted">GitHub sub-rows show: reachability, sync %, untracked local (to add), remote-only (to pull/archive), and ahead/behind. Crypto sub-rows show named buckets (e.g., “handoff archives (3)”) plus key-expiry status.</span>
        <span></span>
      </div>
    </div>
  </div>
</div></body></html>
HTML

echo "[metrics] wrote status/index.html"
