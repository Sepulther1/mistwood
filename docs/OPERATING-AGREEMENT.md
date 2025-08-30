# Mistwood Operating Agreement

**Profile & Browser**
- Use Brave **Mistwood** profile (regular window).
- Tampermonkey installed; “Allow in Private” only if needed.

#next iteration for testing purposes will be in non-private window

**Environment**
- WSL: Ubuntu-24.04
- Repo path: `/home/atlantis/dev/mistwood-dev`
- Python venv: `.venv` (auto-activate)

**VS Code**
- Tasks: Mistwood start/stop/restart/status; tail logs.
- Chords (Ctrl+Alt+…): E, X, R, T, L (tail), Q (stop tail), F (force stop), B (open web).
- Terminals: one shared “Tasks” + one dedicated “Logs”.

**Ops**
- Ops log: `.vscode/ops.log`

**Profile & Browser**
- Use Brave **Mistwood** profile (regular window).
- Tampermonkey installed; “Allow in Private” only if needed.

**Environment**
- WSL: Ubuntu-24.04
- Repo path: `/home/atlantis/dev/mistwood-dev`
- Python venv: `.venv` (auto-activate)

**VS Code**
- Tasks: Mistwood start/stop/restart/status; tail logs.
- Chords (Ctrl+Alt+…): E, X, R, T, L (tail), Q (stop tail), F (force stop), B (open web).
- Terminals: one shared “Tasks” + one dedicated “Logs”.

**Ops**
- Ops log: `.vscode/ops.log`
- Keep terminal count minimal; reuse shared panels.

**Performance**
- Lag tools run in Mistwood profile.
- If chat lags, restart in fresh tab/profile; keep this doc open.

_Last updated: YYYY-MM-DD_

**Performance**
- Lag tools run in Mistwood profile.
- If chat lags, restart in fresh tab/profile; keep this doc open.

_Last updated: YYYY-MM-DD_

_Last updated: 2025-08-21_

## Purpose
Mistwood is our game-first sandbox where people learn, build, and have fun. It doubles as a proving ground for systems we may package for others (developer tooling, performance workflows, simulated economies).

## Environment
- **OS/Runtime:** WSL Ubuntu-24.04, Python 3.12, virtualenv `.venv` (auto-activated)
- **Repo path (WSL):** `/home/atlantis/dev/mistwood-dev`
- **Core server:** Mistwood 5.x

## Editor & Ops
- **VS Code Tasks:** evennia start/stop/restart/status; tail logs; open web
- **Chords (Ctrl+Alt+…):** `E` start, `X` stop, `R` restart, `T` status, `L` tail logs, `Q` stop tail, `F` force-stop, `B` open web
- **Terminals policy:** Reuse **one** shared “Tasks” terminal + **one** dedicated “Logs” terminal
- **Ops log (canonical):** `.vscode/ops.log` (human-readable, append-only)

## Browser Profile
- **Brave profile:** “Mistwood” (Tampermonkey enabled in Private)
- **Userscripts:** LagBar (scroll-lock + UI stability), LagLab Passive (light telemetry)

## Decision Records
- Use ADRs under `docs/ADR/` to capture architecture/ops choices.
- Example: `docs/ADR/0001-ops-choices.md`

## Performance
- We prefer stability and observability over cleverness.
- Quarterly micro-audits; see `docs/PERFORMANCE_PLAYBOOK.md`.

## Security & Ethics
- Simulated finance is **not** real finance. No promises of profit. No financial advice.
- If we later bridge to real-world value, we will add legal/compliance reviews and gates.

## Release Stages
1. **Local (WSL)**
2. **Sandbox (container/VM)**
3. **Beta (invite-only)**
4. **Mature (docs, backups, updates)**

## How we work
- Clear, paste-ready instructions including **file path + where to paste** + a short **why**.
- Keep terminal counts low; keep logs useful; keep fun high.

# Operating Agreement (Out-of-Game, Draft)

Roles, equity placeholders, IP ownership, conflict resolution.  
Not legal advice; for internal planning until formalized.