#!/usr/bin/env bash
set -euo pipefail
cd "${GROVE_ROOT:-$PWD}"

out="docs/status/git-sync.json"
mkdir -p docs/status

greens=(); yellows=(); reds=()

if [ ! -d .git ]; then reds+=("not a git repo"); fi

remote="$(git remote 2>/dev/null | head -n1 || true)"
if [ -z "${remote:-}" ]; then
  yellows+=("no git remote set")
else
  if git ls-remote "$remote" >/dev/null 2>&1; then
    greens+=("remote reachable")
  else
    reds+=("remote auth failed")
  fi
fi

# ahead/behind
branch="$(git rev-parse --abbrev-ref --symbolic-full-name @{u} 2>/dev/null || echo "")"
ahead=0; behind=0
if [ -n "$branch" ]; then
  set +e
  read -r behind ahead <<<"$(git rev-list --left-right --count "$branch"...HEAD 2>/dev/null || echo "0 0")"
  set -e
fi

# worktree stats
tracked=$(git ls-files 2>/dev/null | wc -l | tr -d ' ')
modified=$(git status --porcelain 2>/dev/null | grep -E '^( M|M )' | wc -l | tr -d ' ')
untracked=$(git ls-files --others --exclude-standard 2>/dev/null | wc -l | tr -d ' ')
clean=$(( tracked>0 ? 100*(tracked - modified)/tracked : 100 ))

# remote-only (rough)
remote_only=0
if [ -n "$branch" ]; then
  git fetch -q || true
  tmp_remote=$(mktemp); tmp_local=$(mktemp)
  git ls-tree -r --name-only "$branch" > "$tmp_remote" 2>/dev/null || true
  git ls-files > "$tmp_local"
  remote_only=$(comm -23 <(sort "$tmp_remote") <(sort "$tmp_local") | wc -l | tr -d ' ')
  rm -f "$tmp_remote" "$tmp_local"
fi

# write JSON via Python (values from env)
SYNC_REMOTE="$remote" SYNC_BRANCH="$branch" \
SYNC_TRACKED="$tracked" SYNC_MODIFIED="$modified" SYNC_UNTRACKED="$untracked" \
SYNC_CLEAN="$clean" SYNC_AHEAD="$ahead" SYNC_BEHIND="$behind" SYNC_REMOTE_ONLY="$remote_only" \
python3 - "$out" <<'PY'
import json, sys, os
out = sys.argv[1]
def i(name): 
    try: return int(os.environ.get(name,'0'))
    except: return 0
data = {
  "remote": os.environ.get("SYNC_REMOTE",""),
  "branch": os.environ.get("SYNC_BRANCH",""),
  "stats": {
    "tracked": i("SYNC_TRACKED"),
    "modified": i("SYNC_MODIFIED"),
    "untracked": i("SYNC_UNTRACKED"),
    "clean_pct": i("SYNC_CLEAN"),
    "ahead": i("SYNC_AHEAD"),
    "behind": i("SYNC_BEHIND"),
    "remote_only": i("SYNC_REMOTE_ONLY"),
  }
}
open(out,"w").write(json.dumps(data, indent=2))
print(f"[sync] wrote {out}")
PY

# human lines for dashboard sub-rows
[ ${#reds[@]} -eq 0 ] && [ ${#yellows[@]} -eq 0 ] && echo "green: github-connect basics ok" || true
for x in "${greens[@]}";  do echo "green: $x";  done
for x in "${yellows[@]}"; do echo "yellow: $x"; done
for x in "${reds[@]}";    do echo "red: $x";   done

echo "green: sync coverage ${clean}% (tracked=$tracked, modified=$modified)"
echo "yellow: untracked local files (add → GH): $untracked"
echo "yellow: remote-only files (pull/archive): $remote_only"
echo "green: ahead=$ahead behind=$behind"
