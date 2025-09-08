# Grove Policy (extract)

## WFB Privacy & Rollout (Assistant Rules)
- Treat WFB files as private. Do not propose org-level steps that require reading raw WFB content outside the local machine.
- Use only exposed signals (dashboard JSON, preflight.json) for org-level improvements.
- A/B behavior changes may be applied, but must not require reading private artifacts.
- When a result is validated, convert it into shared policy/wiki — no private content included.

## Handoff Requirement
- A handoff is successful **only if** GitHub connection is verified by the probe.
- If failed: present repair steps; user may keep this instance or terminate and re-run handoff.
- Always run `tools/handoff/preflight.sh` and record the outcome.

