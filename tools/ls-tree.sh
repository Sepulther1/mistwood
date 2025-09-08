#!/usr/bin/env bash
set -euo pipefail
if command -v tree >/dev/null 2>&1; then
  tree -a -I '.venv|__pycache__|.git|*.pyc|node_modules'
else
  find . -path './.venv' -prune -o -path './.git' -prune -o -path '*/__pycache__' -prune -o -print
fi
