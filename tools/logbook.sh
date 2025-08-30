#!/usr/bin/env bash
set -euo pipefail
FILE="/home/atlantis/dev/mistwood-dev-dev/docs/LOGBOOK.md"
TODAY="$(date +%F)"
LINE="- $*"
touch "$FILE"
grep -qE "^## $TODAY$" "$FILE" || printf "\n## %s\n" "$TODAY" >> "$FILE"
printf "%s\n" "$LINE" >> "$FILE"
echo "Appended to $FILE:"
tail -n5 "$FILE"