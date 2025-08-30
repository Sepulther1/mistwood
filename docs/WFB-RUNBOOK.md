# Mistwood Runbook

## Ports (DEV/PROD)
- DEV: telnet 4110, web 4115→4111, websocket 4002
- PROD: telnet 4100, web 4105→4101, websocket **disabled**

## Start/Stop (hotkeys + tasks)
- Ctrl+Alt+E → evennia:start
- Ctrl+Alt+X → evennia:stop
- Ctrl+Shift+R → dev: reload (Mistwood)
…(list the rest)

## Caddy
- Config: `/etc/caddy/Caddyfile`
- Imported sites: `/etc/caddy/sites/mistwood-prod-4105.caddy`, `…4106.caddy`
- All prod sites must start with `http://mistwood.localhost {}` to avoid 308.
- Dev websocket: `127.0.0.1:4002`

## GitHub Actions
- Workflow: `.github/workflows/timelapse-and-telemetry.yml`
- Dispatch: `gh workflow run "timelapse-and-telemetry" --ref <branch> -f ref=<branch> -f CHECK_FINGERPRINT=1`

## PAT/Secrets
- Fine-grained PAT, repo secret `GH_PAT` (read/write Contents, Actions).

## Triage Checklist
1. `ss -ltnp | egrep ':(4002|4004|4105|4115|4100|4110)'`
2. `curl -I http://dev.mistwood.localhost/timelapse/` → 200
3. `curl -I http://mistwood.localhost/healthz` → 200
4. Verify imported Caddy sites start with `http://…`
5. `gh workflow view … --ref main --yaml` shows `workflow_dispatch`

## Snapshot
Run `tools/snapshot.sh` and paste results into new chat to restore context.