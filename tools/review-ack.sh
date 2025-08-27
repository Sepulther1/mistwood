#!/usr/bin/env bash
set -euo pipefail

PATTERN="${1:-}"
BULLETS="${2:-}"
FILE="TODO.md"

# 1) If we have an ack script, try moving NOW → DONE using the pattern
if [[ -n "${PATTERN}" && -x tools/todo-ack.sh ]]; then
  tools/todo-ack.sh "${PATTERN}" || true
fi

# 2) Append a dated 'Session accomplishments' block under '## DONE (recent)'
ts="$(date '+%F %H:%M %Z')"
tmp="$(mktemp)"

awk -v ts="$ts" -v bullets="$BULLETS" '
BEGIN{ins=0}
{
  print $0
  if (!ins && $0 ~ /^##[[:space:]]+DONE[[:space:]]*\(recent\)/) {
    print "### Session accomplishments — " ts
    n = split(bullets, arr, / *; */)
    for (i=1; i<=n; i++) {
      if (length(arr[i])) print "- [x] " arr[i]
    }
    ins=1
  }
}' "$FILE" > "$tmp"

mv "$tmp" "$FILE"
echo "Updated $FILE"
