#!/usr/bin/env python3
from pathlib import Path
import re, sys

ROOTS = [Path("/home/atlantis/dev/mistwood-dev"), Path("/home/atlantis/dev/mistwood-prod")]
SKIP_DIRS = {".git", ".venv", "__pycache__", "server/logs", "web/static", "server/.static"}
SKIP_FILES = {"LICENSE", "LICENSE.txt", "COPYING", "THIRD_PARTY_NOTICES.md"}
EXTS = {".py",".md",".yml",".yaml",".json",".sh",".conf",".caddy",".html",".txt",".mmd"}

PAT = re.compile(r"\bEvennia\b")
APPLY = "--apply" in sys.argv

def walk(base):
    for p in base.rglob("*"):
        if any(part in SKIP_DIRS for part in p.parts): continue
        if p.name in SKIP_FILES: continue
        if p.is_file() and (p.suffix in EXTS or p.suffix == ""):
            yield p

changes = []
for root in ROOTS:
    for f in walk(root):
        t = f.read_text(errors="ignore")
        if PAT.search(t):
            if APPLY:
                f.write_text(PAT.sub("Mistwood", t))
            changes.append(f)

print(("APPLIED " if APPLY else "Would change ") + f"{len(changes)} files.")
for f in changes[:80]: print(" -", f)
if not APPLY and changes:
    print("\nRe-run with --apply to write changes.")