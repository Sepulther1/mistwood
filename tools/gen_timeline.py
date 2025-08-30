#!/usr/bin/env python3
# /home/atlantis/dev/mistwood-dev-dev/tools/gen_timeline.py
from pathlib import Path
import argparse, re

ROOT = Path(__file__).resolve().parents[1]

def parse_logbook(path: Path):
    date = None
    items = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^##\s*(\d{4}-\d{2}-\d{2})", line)
        if m:
            date = m.group(1)
        elif line.startswith("- ") and date:
            items.append((date, line[2:].strip()))
    return items

def build_timeline_mmd(items):
    out = ["timeline", "  title Mistwood build path"]
    last = None
    for d, text in items:
        if d != last:
            out.append(f"  {d} : {text}")
            last = d
        else:
            out.append(f"  : {text}")
    return "\n".join(out) + "\n"

def build_mindmap_mmd(items):
    out = ["mindmap", "  root((Mistwood Evolution))"]
    grouped = {}
    for d, text in items:
        grouped.setdefault(d, []).append(text)
    for d in sorted(grouped.keys()):
        out.append(f"    {d}")
        for t in grouped[d]:
            out.append(f"      {t}")
    return "\n".join(out) + "\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--logbook", default=str(ROOT / "docs" / "LOGBOOK.md"))
    ap.add_argument("--outdir",  default=str(ROOT / "docs"))
    args = ap.parse_args()

    logbook = Path(args.logbook)
    outdir  = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    items = parse_logbook(logbook)

    # Markdown (nice to read in repo)
    md = [
        "# Project Timeline", "",
        "```mermaid", build_timeline_mmd(items).rstrip(), "```", "",
        "# Project Evolution (Mindmap)", "",
        "```mermaid", build_mindmap_mmd(items).rstrip(), "```", ""
    ]
    (outdir / "TIMELINE.md").write_text("\n".join(md), encoding="utf-8")

    # Raw .mmd (for rendering tools)
    (outdir / "TIMELINE-timeline.mmd").write_text(build_timeline_mmd(items), encoding="utf-8")
    (outdir / "TIMELINE-mindmap.mmd").write_text(build_mindmap_mmd(items), encoding="utf-8")

    print(f"Wrote {outdir/'TIMELINE.md'} and .mmd")
if __name__ == "__main__":
    main()