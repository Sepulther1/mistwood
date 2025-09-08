**Transition Score (0–100)** = 100 - min(60, freeze_total_s) - 10*min(3, popups_5m) - overhead
- freeze_total_s: seconds of freeze since last switch
- popups_5m: popups in last 5 minutes
- overhead: 0 (LagBar Prep/New only) or 10 (manual copy), +10 if >1 minute to resume

# Mistwood Workflow

## ACK / Queue protocol
- I send **SUGGESTIONS [n]** with numbered items.
- You reply with **ACK [1,3]** or **ACK ALL**.
- As you finish items, reply **DONE [1]** (or tick them in TODO.md).
- If something is blocked, note **BLOCKED [#]: why**.

## Cadence
- **Start of session:** run `ops:handover pack` task (see below) to show state, verify env, choose 1–3 NOW items.
- **End of session:** tick what’s done, move leftovers, run `ops:handover pack` again; commit with a short note.

## Definition of Done (DoD)
- Code builds/runs, tests pass (if any), tasks.json/keybindings.json updated if relevant, docs updated, logs clean.

# Workflow

- Trunk-based; small PRs; 1 reviewer OK for P2/P3, 2 for P1.
- Conventional Commits; semantic-release drives tags/changelogs.
- Required checks: lint, tests, map generation, packaging (wrappers).

Automation we use:
- GH Actions: lint/test; gen MAP; build Tauri/Capacitor artifacts on tags.
- Pre-commit: ruff/markdownlint, trailing spaces, newline at EOF.
- Issue templates auto-label P1/P2/P3 + area.
- Nightly housekeeping: MAP refresh; stale issue pings.