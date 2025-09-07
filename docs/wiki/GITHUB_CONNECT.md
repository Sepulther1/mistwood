# GitHub Connect (Runbook)

**Success means:** local git remote reachable, and the ChatGPT GitHub connector is authorized & the repo indexed.

## Steps
1. Confirm `git remote -v` and `git ls-remote` succeed (auth OK).
2. Authorize the GitHub connector (org repos may need admin approval).
3. If new/private, force indexing: search `repo:<owner/repo> import` on GitHub; wait up to 5 minutes.
4. Re-run the probe and record the status.

## What the probe reports
- Remote reachable / auth failed
- Sync coverage % (tracked vs modified)
- Untracked local (add to GH)
- Remote-only (pull/archive)
- Ahead/behind counts
