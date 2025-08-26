#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
install -D "$ROOT/docs/timelapse-timeline.mp4" "$ROOT/web/static/timelapse/timeline.mp4"
install -D "$ROOT/docs/timelapse-mindmap.mp4"  "$ROOT/web/static/timelapse/mindmap.mp4"
echo "Published to $ROOT/web/static/timelapse/"
