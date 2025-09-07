#!/usr/bin/env bash
set -euo pipefail
GR="${GROVE_ROOT:-$([ -x ./tools/env/resolve_root.sh ] && ./tools/env/resolve_root.sh || pwd)}"
out="$GR/docs/status/wfb-index.html"
mkdir -p "$GR/docs/status"

tmp="$(mktemp)"
cat > "$tmp" <<'HTML'
<!doctype html><meta charset="utf-8"/><title>WFB Index</title>
<style>
body{font:14px ui-sans-serif,system-ui;margin:24px}
a{color:#1149c9;text-decoration:none} a:hover{text-decoration:underline}
table{border-collapse:collapse;width:100%} th,td{border-bottom:1px solid #ddd;padding:8px;text-align:left}
code{font:12px ui-monospace,monospace} .areas{font:12px ui-monospace,monospace;color:#555}
</style>
<h1>WFB Index</h1>
<table><thead><tr><th>Suggested Chat Title</th><th>File</th><th>Areas</th><th>Date</th></tr></thead><tbody>
HTML

list=$(ls -1t "$GR"/docs/wfb/WFB-*.md "$GR"/docs/wfb.archive/WFB-*.md 2>/dev/null || true)
for f in $list; do
  bn="$(basename "$f")"
  TS="$(echo "$bn" | sed -nE 's/^WFB-([0-9]{8})T([0-9]{6})Z--.*/\1 \2/p')"
  DATE="${TS% *}"; DATE_FMT="$(echo "$DATE" | sed -E 's/^([0-9]{4})([0-9]{2})([0-9]{2})$/\1-\2-\3/')"
  PROJECT="$(echo "$bn" | sed -nE 's/^WFB-[0-9TZ]+--([^-]+)-.*/\1/p')"
  AREAS="$(echo "$bn" | sed -nE 's/^WFB-[0-9TZ]+--[^-]+-([^ ]+)-[0-9]{3}-.*/\1/p')"
  SEQ="$(echo "$bn" | sed -nE 's/^.*-([0-9]{3})-.*$/\1/p')"
  title="$(echo "$PROJECT" | sed 's/.*/\u&/') · $AREAS · $SEQ · $DATE_FMT"
  rel="$(python3 - "$f" <<'PY'
import os,sys
gr=os.environ.get("GR","")
f=sys.argv[1]
print(os.path.relpath(f, os.path.join(gr,"docs","status")))
PY
)"
  echo "<tr><td>${title}</td><td><a href=\"${rel}\"><code>${bn}</code></a></td><td class=\"areas\">${AREAS}</td><td>${DATE_FMT}</td></tr>" >> "$tmp"
done

echo "</tbody></table>" >> "$tmp"
mv "$tmp" "$out"
echo "[wfb] wrote $out"
