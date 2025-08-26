#!/usr/bin/env bash
set -euo pipefail
ROOT="/home/atlantis/dev/mistwood-dev"
DOCS="$ROOT/docs"
OUT="$DOCS"
TMP="$DOCS/.timelapse-tmp"
mkdir -p "$TMP"

if ! command -v mmdc >/dev/null 2>&1; then
  echo "mmdc not found. Run: source ~/.nvm/nvm.sh && nvm use 22 && npm i -g @mermaid-js/mermaid-cli"
  exit 1
fi

TIMELINE_MMD="$DOCS/TIMELINE-timeline.mmd"
MINDMAP_MMD="$DOCS/TIMELINE-mindmap.mmd"
[[ -f "$TIMELINE_MMD" ]] || { echo "Missing $TIMELINE_MMD"; exit 1; }
[[ -f "$MINDMAP_MMD"  ]] || { echo "Missing $MINDMAP_MMD";  exit 1; }

echo "Generating single mermaid chart"
mmdc -i "$TIMELINE_MMD" -o "$TMP/timeline.png"
mmdc -i "$MINDMAP_MMD"  -o "$TMP/mindmap.png"

vf='scale=trunc(iw/2)*2:trunc(ih/2)*2,format=yuv420p'
ffmpeg -y -loop 1 -t 8 -r 24 -i "$TMP/timeline.png" -vf "$vf" "$OUT/timelapse-timeline.mp4"
ffmpeg -y -loop 1 -t 8 -r 24 -i "$TMP/mindmap.png"  -vf "$vf" "$OUT/timelapse-mindmap.mp4"

echo "Wrote:"
ls -lh "$OUT"/timelapse-*.mp4
