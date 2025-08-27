#!/usr/bin/env python3
# /home/atlantis/dev/mistwood-dev/tools/gen_map.py
import json, re, subprocess
from pathlib import Path
from urllib.parse import quote
import subprocess, json

ROOT = Path(__file__).resolve().parents[1]
MAP_MD = ROOT / "docs" / "MAP.md"

NODE_TO_LABELS = {
    "Review-ack": ["review-ack"],
    "Telemetry":  ["telemetry"],
    "Ops":        ["area:ops"],
    "Docs":       ["docs"],
    "Integrations":["integrations"],
}

PRIORITIES = ["P1","P2","P3"]

def have(cmd):
    from shutil import which
    return which(cmd) is not None

def gh_api_json(args):
    try:
        out = subprocess.check_output(args, text=True, stderr=subprocess.DEVNULL)
        return json.loads(out)
    except Exception:
        return {}

def get_repo():
    if have("gh"):
        try:
            return subprocess.check_output(
                ["gh","repo","view","--json","nameWithOwner","-q",".nameWithOwner"],
                text=True
            ).strip()
        except Exception:
            pass
    try:
        url = subprocess.check_output(["git","remote","get-url","origin"], text=True).strip()
        m = re.search(r"[:/](?P<owner>[^/]+)/(?P<repo>[^/.]+)(?:\.git)?$", url)
        if m: return f"{m.group('owner')}/{m.group('repo')}"
    except Exception:
        pass
    return None

def count_open(repo, labels):
    if not repo or not have("gh"):
        return 0
    q = " ".join(['repo:'+repo, "is:issue", "state:open"] + [f'label:\"{l}\"' for l in labels])
    try:
        data = gh_api_json(["gh","api","/search/issues","-f",f"q={q}"])
        return int(data.get("total_count",0))
    except Exception:
        return 0

def link(repo, labels, open_only):
    if not repo:
        return "#"
    terms = []
    if open_only:
        terms += ["is%3Aopen","is%3Aissue"]
    for l in labels:
        terms.append("label%3A" + quote(l))
    return f"https://github.com/{repo}/issues?q=" + "+".join(terms)

def pick_priority(repo, base_labels):
    for i,p in enumerate(PRIORITIES, start=1):
        if count_open(repo, base_labels+[p]) > 0:
            return f"p{i}"
    return "p3"

def recolor_mermaid(repo, text):
    for node, labels in NODE_TO_LABELS.items():
        cls = pick_priority(repo, labels)
        pattern = re.compile(rf"^(\s*{re.escape(node)})(?:::p[123])?", re.MULTILINE)
        text = pattern.sub(rf"\1:::{cls}", text)
    return text

def replace_section(text, begin, end, payload):
    if begin in text and end in text:
        return re.sub(re.escape(begin)+r".*?"+re.escape(end),
                      begin + "\n" + payload + end, text, flags=re.S)
    else:
        return text.rstrip()+"\n\n"+begin+"\n"+payload+end+"\n"

def regen_quicklinks(repo):
    lines = ["## Quick Links",""]
    if not repo:
        lines.append("- _(GitHub repo not detected; run `git remote -v` or `gh auth login`)_")
        return "\n".join(lines) + "\n"
    for node, labels in NODE_TO_LABELS.items():
        open_count = count_open(repo, labels)
        open_url = link(repo, labels, True)
        all_url  = link(repo, labels, False)
        lines.append(f"- **{node}** → [open ({open_count})]({open_url}) · [all]({all_url})")
    return "\n".join(lines) + "\n"

def main():
    repo = get_repo()
    md = MAP_MD.read_text(encoding="utf-8")
    md = recolor_mermaid(repo, md)
    quick = regen_quicklinks(repo)
    md = replace_section(md, "<!-- QUICKLINKS:BEGIN -->", "<!-- QUICKLINKS:END -->", quick)
    MAP_MD.write_text(md, encoding="utf-8")
    print(f"Updated {MAP_MD} (repo={repo or 'unknown'})")

if __name__ == "__main__":
    main()
print("Updated docs/MAP.md Quick Links.")
print("Tip: open it in VS Code and use Markdown Preview (Ctrl+K V).")