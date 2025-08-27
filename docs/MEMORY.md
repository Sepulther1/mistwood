# Grove — Project Memory

**Purpose:** Capture durable decisions, conventions, and prompts we want the AI to nudge on.

## Conventions
- After any meaningful chunk, run **review-ack** (NOW→DONE + session bullets).
- Always use **absolute paths** in instructions.
- Prefer **tasks + hotkeys**; keep README short.

## Categories
- Visual (UI/UX, dashboards, maps)
- Technical (Evennia, commands, ports, profiling)
- Ops (tasks.json, hotkeys, scripts)
- Telemetry (metrics, dashboards, alerts)
- Product (scope, loops, monetization)
- Integrations (APIs/devices, auth, streaming)
- Docs (CHECKLIST, PRODUCTIZE, OPERATIONS)

## Prompts to self (nudges)
- “Run review-ack now?”
- “Open ops:health before merge?”
- “Did you pin ports in settings.py for this env?”

## Running Log (append at top)
- 2025-08-22: Baseline memory created.

# Decision Log (ADR-Lite)

Template:
- **Context**
- **Decision**
- **Rationale**
- **Alternatives**
- **Date / Owners**
- **Links** (PRs, issues)

## Entries
- Ports Policy → WS on 4102; internal web on 4105; AMP 4106. (2025-08-24)
- Conventional Commits + semantic-release. (…)
- MAP automation via tools/gen_map.py. (…)

- CLI-first: for any action, prefer a paste-ready bash snippet over point-and-click.
- Always include **absolute paths** and the **exact file path** above code blocks.
- When giving multi-file changes, include a **both-repos** bash loop.

## Prompts to self (nudges)
- “Did I include absolute paths and a both-repos CLI?”
- “Did I show 'where to paste' and 'why' for each file block?”