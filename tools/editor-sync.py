#!/usr/bin/env python3
import json, shutil, os
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SRC  = REPO/"editor"/"vscode"/"keybindings.json"
LOCAL_OVR = REPO/"editor"/"vscode"/"keybindings.local.json"

def load(p: Path): return json.loads(p.read_text()) if p.exists() else []
def dedupe(arr):
    seen=set(); out=[]
    for kb in arr:
        key=(kb.get("key"), kb.get("command"), json.dumps(kb.get("args",None), sort_keys=True))
        if key not in seen: seen.add(key); out.append(kb)
    return out

def write(dst: Path, merged):
    dst.parent.mkdir(parents=True, exist_ok=True)
    b=dst.with_suffix(".json.bak")
    if dst.exists() and not b.exists(): shutil.copy2(dst, b)
    dst.write_text(json.dumps(merged, indent=2))
    print("Synced", dst)

repo=load(SRC); ovr=load(LOCAL_OVR)

# 1) Linux (remote)
linux_dst = Path.home()/".config/Code/User/keybindings.json"
cur=load(linux_dst); merged=dedupe(ovr+repo+[x for x in cur if x not in (ovr+repo)])
write(linux_dst, merged)

# 2) Windows (local UI when using WSL)
win_dst = Path("/mnt/c/Users/justi/AppData/Roaming/Code/User/keybindings.json")
if win_dst.exists() or win_dst.parent.exists():
    curw=load(win_dst); mergedw=dedupe(ovr+repo+[x for x in curw if x not in (ovr+repo)])
    write(win_dst, mergedw)