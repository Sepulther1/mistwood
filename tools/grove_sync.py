#!/usr/bin/env python3
from pathlib import Path, PurePosixPath
import json, subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT  = ROOT / "web" / "static" / "telemetry"
OUT.mkdir(parents=True, exist_ok=True)

def run(cmd: str) -> str:
    return subprocess.check_output(cmd, shell=True, text=True).strip()

try:
    commits = int(run("git rev-list --count HEAD"))
except Exception:
    commits = 0

grade = "A" if commits > 50 else "B" if commits > 20 else "C"
payload = {"grade": grade, "commits": commits}

path = OUT / "grade.json"
path.write_text(json.dumps(payload, indent=2))
print("Wrote", PurePosixPath(path))
