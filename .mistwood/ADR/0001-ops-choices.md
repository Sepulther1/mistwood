# ADR 0001: Ops conventions (tasks, terminals, logs)
Date: 2025-08-20
Status: Accepted

## Context
We run Evennia from VS Code on WSL. We want low-friction controls and reproducible logs.

## Decision
- Use VS Code tasks with chords Ctrl+Alt+E/X/R/T/L/Q/F/B
- Reuse one “Tasks” terminal + one “Logs” terminal
- Log all ops to `.vscode/ops.log`
- Keep persistent prefs in `.mistwood/MEMORY.md`

## Consequences
- Faster onboarding and consistent ops
- Easy packaging for others

# ADR 0001 — Ops conventions
Date: 2025-08-21 — Status: Accepted

- VS Code tasks + chords
- One shared Tasks terminal + one dedicated Logs terminal
- Append to `.vscode/ops.log`
- Use docs/ for persistent knowledge