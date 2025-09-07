#!/usr/bin/env bash
set -euo pipefail
GR="${GROVE_ROOT:-$PWD}"
cd "$GR"
mkdir -p docs/status

pass=1
msgs=()

# A) Dashboard builds
if "$GR/tools/metrics/compute.sh" >/dev/null 2>&1; then
  msgs+=("green: dashboard rendered")
else
  msgs+=("red: dashboard render failed"); pass=0
fi

# B) GitHub probe
if [ -x "$GR/tools/git/sync_report.sh" ]; then
  gh="$("$GR/tools/git/sync_report.sh" 2>/dev/null || true)"
  if echo "$gh" | grep -qi '^red:'; then
    msgs+=("red: github probe found blockers"); pass=0
  else
    msgs+=("green: github probe ok")
  fi
  printf '%s\n' "$gh" > docs/status/git-sync.lines
else
  msgs+=("red: missing tools/git/sync_report.sh"); pass=0
fi

# C) WFB index present
if [ -f docs/status/wfb-index.html ]; then
  msgs+=("green: WFB index present")
else
  if "$GR/tools/wfb/build_index_page.sh" >/dev/null 2>&1; then
    msgs+=("yellow: WFB index was missing; built now")
  else
    msgs+=("red: WFB index missing and failed to build"); pass=0
  fi
fi

# D) Active WFB header + TODOs
latest="$(ls -1t docs/wfb/WFB-*.md 2>/dev/null | head -n1 || true)"
if [ -n "$latest" ] && [ -f "$latest" ]; then
  if head -n1 "$latest" | grep -q '^---'; then
    msgs+=("green: WFB header present ($(basename "$latest"))")
  else
    msgs+=("red: WFB header missing in $(basename "$latest")"); pass=0
  fi
  todo_count=$(grep -E '(^|[[:space:]])(TODO:|TODO\b|^- \[ \])' "$latest" | wc -l | tr -d ' ')
  if [ "${todo_count:-0}" -ge 5 ]; then
    msgs+=("green: TODOs present ($todo_count)")
  else
    msgs+=("yellow: few TODOs ($todo_count < 5)")
  fi
else
  msgs+=("red: no WFB files found"); pass=0
fi

# E) Crypto current bundle present (advisory)
if grep -qi '^green: wfb current' docs/status/index.html 2>/dev/null; then
  msgs+=("green: crypto current bundle present")
else
  msgs+=("yellow: crypto current bundle missing (seal current WFB)")
fi

status=$([ "$pass" -eq 1 ] && echo "green" || echo "yellow")

# Write JSON with Python (never fails silently)
PY_STATUS="$status" PY_LINES="$(printf '%s\n' "${msgs[@]}")" \
python3 - <<'PY'
import json, os, pathlib
out = pathlib.Path("docs/status/preflight.json")
lines = [l for l in os.environ.get("PY_LINES","").splitlines() if l.strip()]
data = {"status": os.environ.get("PY_STATUS","yellow"), "notes": lines}
out.write_text(json.dumps(data, indent=2))
print(f"[preflight] wrote {out}")
PY

# Human-readable echo
printf '%s\n' "${msgs[@]}"
echo "$status: handoff preflight"
