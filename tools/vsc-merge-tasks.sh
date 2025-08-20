#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
TASKS_FILE=".vscode/tasks.json"
BACKUP=".vscode/tasks.json.bak.$(date +%Y%m%d-%H%M%S)"

# Read desired tasks JSON from stdin, merge by .label, ensure 'needle' input exists.
cp "$TASKS_FILE" "$BACKUP" 2>/dev/null || true
jq --slurpfile desired /dev/stdin '
  (.[0] // {}) as $desired |
  . as $orig |
  ($orig.version // "2.0.0") as $ver |
  ($orig.tasks // []) as $tasks |
  ($desired[0].tasks // $desired[0] // []) as $want |
  ($tasks + $want | unique_by(.label)) as $merged |
  ($orig.inputs // []) as $inputs |
  ($inputs | (map(select(.id=="needle")) | length) as $has |
     if $has==0 then . + [ { "id":"needle","type":"promptString","description":"Search text:","default":"" } ] else . end
  ) as $inputs2 |
  { "version": $ver, "tasks": $merged, "inputs": $inputs2 }
' "$TASKS_FILE" > .vscode/tasks.tmp && mv .vscode/tasks.tmp "$TASKS_FILE"
echo "Merged. Backup at $BACKUP"
