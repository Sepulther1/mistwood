# Case Study: Error Burst (2025-09-06)

**Symptom:** many commands failed with `No such file or directory` for `/tools/...` and `/.mistwood/...`.

**Root causes:**
- `$GR` was empty (new shell), so `$GR/tools/...` expanded to `/tools/...`.
- Some here-doc blocks were executed in the shell instead of being written to files.
- WSL interop confused browser opening; fixed by serving `http://localhost:8000`.

**Fixes implemented:**
- Added `grcd` (always export a valid `$GR`) and `gr_write` (write files under `$GR` safely).
- Standardized preview via `python3 -m http.server 8000`.
- Policy requiring path guardrails; ACTIVE WFB skip in batch scripts.

**Prevention:**
- Every WFB includes `policy.ref` + preflight results.
- Probes re-run after each remedial action with status recorded.
