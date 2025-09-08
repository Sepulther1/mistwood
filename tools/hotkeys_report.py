#!/usr/bin/env python3
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
repo = json.loads((REPO/"editor/vscode/keybindings.json").read_text())
userp = Path.home()/".config/Code/User/keybindings.json"
user = json.loads(userp.read_text()) if userp.exists() else []

def key(x): return (x.get("key"), x.get("command"), json.dumps(x.get("args", None), sort_keys=True))
rset, uset = {key(x) for x in repo}, {key(x) for x in user}

only_repo = [x for x in repo if key(x) not in uset]
only_user = [x for x in user if key(x) not in rset]

out = REPO/"web/static/docs"
out.mkdir(parents=True, exist_ok=True)
md = out/"hotkeys.md"
def fmt(arr):
    return "\n".join(f"- `{k}` → `{c}`{(' ('+str(a)+')') if a else ''}"
                     for k,c,a in ((x.get('key'),x.get('command'),x.get('args')) for x in arr))

md.write_text(
    "# Grove Hotkeys\n\n## Standard\n\n"+fmt(repo)+
    "\n\n## Your extra hotkeys\n\n"+fmt(only_user)+
    "\n\n---\n\n### Opt-out / local overrides\n"
    "Create the file:\n\n"
    "`/home/atlantis/dev/mistwood-dev/editor/vscode/keybindings.local.json`\n\n"
    "Put `[]` to disable all repo defaults on this machine, or put your own bindings.\n"
    "The sync tool merges **local overrides > repo defaults > your existing user keys**.\n"
)
print("Wrote", md)