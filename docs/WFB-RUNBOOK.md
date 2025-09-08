# Mistwood Runbook

## 0. Start Here (Daybook)
- Today’s goal:
- Current blockers:
- Last known good snapshot: `docs/SNAPSHOT.txt` (date/time)

## 1. Ports & Processes
- DEV: telnet 4110, web 4115→4111, websocket 4002
- PROD: telnet 4100, web 4105→4101, websocket **disabled**
- Commands:
  - List: ss -ltnp | egrep ':(4002|4004|4012|4105|4115|4100|4110)'
  - Stop/start: tools/ev.sh {stop|start|status|logs|force-stop}
- Known pitfalls:
  - PROD websocket must be off: `WEBSOCKET_CLIENT_ENABLED=False`, `WEBCLIENT_PORTS=[]`.

## 2. Caddy
- Files: /etc/caddy/Caddyfile; /etc/caddy/sites/mistwood-prod-4105.caddy; …4106.caddy
- Rules of thumb:
  - All sites must start with `http://…` to avoid 308.
  - DEV `/ws` → 127.0.0.1:4002
  - Health check: `/healthz`
- Useful:
  - Validate+reload: task “caddy: validate+reload” (Ctrl+Shift+C)
  - Verify site hosts: tools/verify_caddy_hosts.py

## 3. GitHub Actions
- Workflow: .github/workflows/timelapse-and-telemetry.yml (on `main`)
- Secrets: `GH_PAT` (Contents RW, Actions RW)
- Dispatch:
  - VS Code task (Ctrl+Shift+D), or:
  - `gh workflow run "timelapse-and-telemetry" --ref <branch> -f ref=<branch> -f CHECK_FINGERPRINT=1`
- Troubleshooting:
  - 422 = workflow not on `main` or wrong `inputs` names.

## 4. Hotkeys
- Standard keys (list your favorites): Ctrl+Alt+E/X/R/T/L/Q/F/B; Ctrl+Shift+R/S/G/T/D/C
- How to regenerate docs: tools/hotkeys_report.py → web/static/docs/hotkeys.md
- Opt-out: `editor/vscode/keybindings.local.json` (use `[]` to disable repo keys on a machine)

## 5. Naming/Branding
- “Evennia → Mistwood” policy:
  - Do rename human-readable mentions.
  - Do **not** rename legal notices or code imports (`import evennia`).
- Script: tools/rename_evennia_to_mistwood.py (safe mode) + verification steps.

## 6. Editor & Saving
- Use `sudoedit` with `SUDO_EDITOR="code --wait"` for `/etc/*`.
- If VS Code says “file is newer”: File → Revert File, then re-apply.

## 7. Handoff / New Chat Window
- Generate snapshot: tools/snapshot.sh > docs/SNAPSHOT.txt
- Update runbook + hotkeys: commit/push (use `--no-verify` if pre-commit missing)
- Paste the last 30 lines of:
  - `ss -ltnp …`
  - `curl -I http://dev.mistwood.localhost/timelapse/`
  - `curl -I http://mistwood.localhost/healthz`
  - Any failing logs (portal.log, server.log)

## 8. Known Issues & Fix Recipes
- “PROD failed to start with 4002 in use” → see §1.
- “DEV returns 308” → add `http://` scheme in Caddy.
- “Workflow 422” → ensure on `main` and inputs match.
- “Hotkeys not working” → fix Windows JSON, run editor-sync.py, Reload Window.

## 9. Appendix (One-liners)
- sed patches we use often (host scheme, ws proxy, etc.)
- gh commands (view runs, view logs)
- evennia management shortcuts (tools/ev.sh)

## Triage Checklist
1. `ss -ltnp | egrep ':(4002|4004|4105|4115|4100|4110)'`
2. `curl -I http://dev.mistwood.localhost/timelapse/` → 200
3. `curl -I http://mistwood.localhost/healthz` → 200
4. Verify imported Caddy sites start with `http://…`
5. `gh workflow view … --ref main --yaml` shows `workflow_dispatch`