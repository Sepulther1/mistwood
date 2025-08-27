# Performance Playbook

## Goals (What “good” looks like)
- **Fast UI:** No surprise scroll jumps; chat/terminal actions feel instant.
- **Low friction dev loop:** Start/stop/restart tasks in a single terminal; logs in one dedicated terminal.
- **Observable:** Ops events and errors land in `.vscode/ops.log`.

## Cadence
- **Weekly:** Quick glance at `.vscode/ops.log` after start → restart → stop flows.
- **Quarterly:** 1-hour micro-audit (UI smoothness, task speed, log quality, terminal reuse).

## KPIs (track lightly in a checklist or CSV if helpful)
- UI latency (perceived): start/restart < 3s, web open < 1s.
- Terminal count: ≤ 2 (1 shared Tasks + 1 Logs).
- Error rate in ops.log: near-zero during routine flows.
- Page stability: no forced scroll jumps during replies.

## Practices & Checklists

### Frontend (Chat/Browser)
- **Prevent auto-jumps:** userscript scroll-lock (LagBar) enabled by default.
- Lazy-load heavy assets; no blocking JS.
- Avoid excessive DOM churn in chat view.

### VS Code / Tasks
- Reuse panels (`"panel": "shared"`), use one dedicated “Logs”.
- Append timestamps to `.vscode/ops.log`.
- Prefer `bash -lc 'source .venv/bin/activate && …'`.

### Backend / Server
- Keep Evennia + Twisted updated (security fixes).
- Log actionable errors; avoid noisy stacktraces.

### Data & Caching
- Cache static assets if/when we host web assets separately.
- Profile DB queries before adding features with heavy data access.

### Culture & Training
- Encourage small, reversible changes.
- Document wins and pitfalls for others.

## Tooling Ideas (Backlog)
- “LagLab Passive” tiny footer widget for session timing/connection info.
- Optional telemetry CSV (local-only) for task durations.

# Performance Playbook

Targets: p50 50ms / p95 200ms for common commands at N=100 concurrent.

Smoke (local):
- 20–50 dummy WS clients sending `look`/`help` every 3–5s.
- Track CPU, RSS, GC pauses; record portal.log timings.

Capacity Plan:
- One-box goal: 300 concurrent stable. Scale via sharding realms later.

Next:
- Add a `load/` dir with a simple Python WS swarm (todo).
- Grafana panels for command latency, WS connections, errors.