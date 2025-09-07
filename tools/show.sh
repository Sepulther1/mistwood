#!/usr/bin/env bash
set -euo pipefail
file="$1"
nl -ba "$file" | sed -n '1,200p'
