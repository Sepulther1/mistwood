# Epic: Error Guards — path hygiene & ACTIVE safety

- [ ] Add a tiny `tools/guard/gr_required.sh` sourced by any script that writes files (exit if `$GR` missing).
- [ ] Ensure `set -euo pipefail` at top of all scripts that modify files.
- [ ] Make batch WFB tools skip the ACTIVE file (already done for headers; extend to any renamers).
- [ ] Create `gr_write`-style helper for scripts (use `install -D`).
- [ ] Add dashboard badge: “Policy Preflight” last result (green/yellow/red) with a link to the WFB.
