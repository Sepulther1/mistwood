#!/usr/bin/env bash
# tools/todo-ack.sh
# Move matching NOW bullets in TODO.md to DONE (recent) with timestamp.
# Usage:
#   tools/todo-ack.sh "<regex pattern>"
#   tools/todo-ack.sh --dry-run "<regex pattern>"

set -euo pipefail
cd "$(dirname "$0")/.."

TODO="TODO.md"
DRY=0
if [[ "${1-}" == "--dry-run" ]]; then
  DRY=1
  shift || true
fi

if [[ $# -lt 1 ]]; then
  echo "Usage: tools/todo-ack.sh [--dry-run] <regex pattern>" >&2
  exit 2
fi

PATTERN="$1"
TS="$(date '+%F %T')"

if [[ ! -f "$TODO" ]]; then
  echo "error: $TODO not found in repo root." >&2
  exit 1
fi

tmp="$(mktemp)"
mvout="$(mktemp)"   # collected matches to insert under DONE

# Parse & transform with awk:
# - Track when inside NOW and DONE sections.
# - Collect matching NOW bullets to mvout (with [x] and timestamp).
# - Remove those bullets from NOW in the output.
# - On the first DONE (recent) header, inject collected lines immediately after.
awk -v IGNORECASE=1 -v pat="$PATTERN" -v mvout="$mvout" -v ts="$TS" '
  BEGIN {
    in_now=0; in_done=0; injected=0; moved=0;
  }
  function is_header_now(line)      { return line ~ /^##[[:space:]]+NOW[[:space:]]*$/ }
  function is_header_done(line)     { return line ~ /^##[[:space:]]+DONE[[:space:]]*\(recent\)[[:space:]]*$/ }
  function is_bullet(line)          { return line ~ /^- [\[\(][ xX][\]\)] / }  # - [ ] or - ( )
  function matches(line)            { return line ~ pat }

  {
    if (is_header_now($0))  { in_now=1;  in_done=0; print $0; next }
    if ($0 ~ /^##[[:space:]]+/) { in_now=0 }  # leaving NOW on any new H2

    if (is_header_done($0)) { in_done=1; print $0;
      # Inject moved lines right after header (only once)
      if (!injected) {
        while ((getline l < mvout) > 0) {
          print l
          injected=1
        }
        close(mvout)
      }
      next
    }
    if ($0 ~ /^##[[:space:]]+/) { in_done=0 }  # leaving DONE on any new H2

    # When in NOW: drop matching bullets and collect them to mvout
    if (in_now && is_bullet($0) && matches($0)) {
      # Normalize to [x] and append timestamp
      line=$0
      sub(/^- [\[\(][ xX][\]\)] /, "- [x] ", line)
      printf("%s — ACK %s\n", line, ts) >> mvout
      moved++
      next
    }

    # Else: keep line
    print $0
  }
  END {
    if (moved == 0) {
      # If nothing matched, ensure mvout is closed and empty so caller knows.
      close(mvout)
      # Emit a special marker line to stderr (not stdout)
      # (stdout is the transformed file stream)
      # We cannot write to stderr from AWK END portably across all awks; just print marker.
      print "##__NO_MOVES__##" > "/dev/stderr"
    }
  }
' "$TODO" > "$tmp" 2> "$tmp.stderr" || true

if grep -q "##__NO_MOVES__##" "$tmp.stderr"; then
  echo "No NOW bullets matched pattern: $PATTERN"
  rm -f "$tmp" "$tmp.stderr" "$mvout"
  exit 0
fi

if [[ $DRY -eq 1 ]]; then
  echo "DRY-RUN: would update $TODO with the following DONE lines:"
  echo "--------------------------------------------------------"
  cat "$mvout" || true
  echo "--------------------------------------------------------"
  rm -f "$tmp" "$tmp.stderr" "$mvout"
  exit 0
fi

cp -f "$TODO" "$TODO.bak.$(date +%s)"
mv -f "$tmp" "$TODO"
rm -f "$tmp.stderr" "$mvout"

echo "ACK complete: updated $TODO"