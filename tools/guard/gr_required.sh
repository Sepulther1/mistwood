#!/usr/bin/env bash
set -euo pipefail
: "${GR:?Set GR first (run grcd).}"
[ -d "$GR" ] || { echo "[guard] GR directory missing: $GR" >&2; exit 2; }
