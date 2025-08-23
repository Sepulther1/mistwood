# TODO (Mistwood)

## NOW (keep 1–3 max)
- [ ] …
Create tools/ev.sh and chmod +x (Suggestion 3).

Fix tasks.json “telemetry:open dashboard” entry (Suggestion 4).

Add telemetry/server.py, then run telemetry:install → telemetry:start → telemetry:open dashboard (Suggestions 5–6).
## NEXT
- [ ] …
4. Apply keybinding fixes (Suggestion 7).
5. Add docs/OPERATIONS.md and (optionally) .github/ISSUE_TEMPLATE/task.md (Suggestions 8–9).
6. Add the Transition Score formula to docs/WORKFLOW.md (Suggestion 10).
## BACKLOG
- [ ] …

## BLOCKED
- [ ] …

## DONE (recent)
### Session accomplishments — 2025-08-22 18:16 PDT
- [x] Fixed WEBSERVER_PORTS tuple
- [x] Restored default_cmdsets.py
- [x] Wired @rld
- [x] Telemetry tasks verified
### Session accomplishments — 2025-08-22 17:35 PDT
- [x] Fixed WEBSERVER_PORTS tuple
- [x] Replaced default_cmdsets.py
- [x] Wired @rld
- [x] Added issue template
- [x] review-ack script working
### Session accomplishments — 2025-08-22 13:01 PDT
- [x] Fixed Evennia ports: WEBSERVER_PORTS = [(4001, 4005)] → Server RUNNING; wired @rld hot-reload; added GitHub task template; ack hotkey set.
### Session accomplishments — 2025-08-22 12:04 PDT
- [x] `tools/ev.sh` created + `chmod +x`; start/stop/restart/status/tail/force-stop/open-web wired.
- [x] `commands/ping.py` implemented; `CmdPing` registered once per cmdset; verified `ping → PONG` in MushClient/webclient.
- [x] Keybinding conflicts fixed; ops/ADR/doc hotkeys added.
- [x] `docs/OPERATIONS.md` added; Transition Score formula added to `docs/WORKFLOW.md`.
- [x] Telemetry scaffold: `telemetry/server.py` added; VS Code tasks: `telemetry:install`, `telemetry:start`, `telemetry:open dashboard`.
- [x] Dev profiling task added: `dev:profile reload` + `.vscode/importtime_summary.py`.
- [x] `TODO.md` hygiene: ACKed ping items into **DONE**; removed from **NOW**.
- [x] `tools/todo-ack.sh` added (+ task `todo:ack`); `tasks.json` validated.
- [x] Register `CmdPing` once per cmdset (Character, Account, Unloggedin).
- [x] Evennia portal/server running clean after reload (no import errors).
- [x] Verified `ping` → `PONG from Evennia!` in MushClient (localhost:4000) and webclient (http://localhost:4001).
- [x] …
3× self.add(CmdPing()) (one per cmdset) ✅

Evennia up, portal/server healthy ✅

ping → PONG from Evennia! ✅
