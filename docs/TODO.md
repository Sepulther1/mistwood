TODO (living)
Now

Fix Mermaid parse edge-cases in TIMELINE-*.mmd (sanitizer added).

Ensure websocket shows 4102 in Portal banner.

Publish timelapse to /static/timelapse/ and verify page.

Next

Wire tools/grove_sync.py into a VSCode Task and cron/GitHub Action.

Expose Grove grade + metrics as charts on /dashboard/.

Later

Grove⇄GitHub: issue/PR sync → grove/state.json, labels back to GH.

Webclient UX polish; add health pings & latency in dashboard.

Blocked

None right now.
- [ ] Audit VS Code tasks/ev.sh to use mistwood-dev paths only (blocker for clean restarts)
- [ ] Public mirror for AI review (or temporarily make repo public) so assistant can audit helpers/paths.
- [ ] Audit VS Code tasks and tools/ev.sh to use /home/atlantis/dev/mistwood-dev-dev/.venv (no references to /home/atlantis/dev/mistwood-dev).
- [ ] One-time DEPLOY_KEY fingerprint check in CI (remove after verifying).
- [ ] Clean workflow: single job, runs-on: self-hosted; remove ubuntu-latest duplicate.
- [ ] Blue/green layout: prod vs dev instances on separate ports; proxy cut-over with Caddy/Nginx.
- [ ] Branding: replace Mistwood name where appropriate (keep copyright/attribution).
- [ ] Website pass: ensure /dashboard and pages show telemetry, grades, links, docs.
- [ ] Legal: draft OSS/proprietary split, license files, attribution, and trademark plan; add “How we license” page.
- [ ] Device matrix: test telnet, webclient, websocket; document ports and connection options.
- [ ] Make deploy step local on self-hosted runner (no SSH).
- [ ] Add real checks to grove_sync (GitHub checks, port probes, artifact freshness).
- [ ] Blue/green prod vs dev; Caddy cut-overs.
- [ ] “How we license Mistwood” page & docs attribution for Mistwood.
- [ ] Public mirror (or confirm repo stays public) for AI audits.
- [ ] Create GH labels (chore, infra, legal, docs) with gh CLI (needs repo scope).
- [ ] Device matrix (telnet, webclient, websocket) and connection docs.
- [ ] Convert deploy to local (done), remove SSH from workflow.
- [x] Helpers audit; fix site routes; switch workflow to local reload; add fingerprint input; Caddy fixed.
- [ ] Draft “How we license Mistwood” full page and link in nav
- [ ] Private-content scaffolding: pull private repo at deploy; templated stubs

Done:
✅ Created and chmod’d tools/ev.sh (start/stop/restart/status/tail/force-stop/open-web).

✅ Fixed VS Code task telemetry:open dashboard.

✅ Added telemetry/server.py and wired install/start/open tasks (page loads; initial “did not connect” will be resolved by the Passive script replacement + POST test above).

✅ Resolved keybinding conflicts; added ops:handover pack hotkey.

✅ Added docs/OPERATIONS.md.

✅ Added Transition Score formula to docs/WORKFLOW.md.

✅ CmdPing implemented and registered once per cmdset; verified in MushClient and webclient.

✅ Evennia start/stop/restart/status tasks + tools/ev.sh are working.

✅ Ports for your dev instance show as expected (4000/4001/4002/4005).

✅ TODO update: you already moved “CmdPing” work into DONE and pruned NOW (commit docs(todo): ACK ping work in DONE and prune NOW).

CmdPing wiring & verification: 100%
Port config (Evennia): 100%

Fix Evennia ports (prod): server/conf/settings.py → TELNET_PORTS=[4000], WEBSERVER_PORTS=[(4001,4005)], WEBSOCKET_CLIENT_PORTS=[4002]

Custom commands wired & verified: commands/ping.py (ping), commands/devtools.py (@rld)

commands/default_cmdsets.py repaired (no heredoc), CmdReloadCommands added to Account cmdset

Telemetry scaffold running: uvicorn telemetry.server:app → /metrics OK

tools/review-ack.sh executable + “quick” task appears

Helper ops scripts: tools/health.sh, tools/ls-tree.sh, tools/show.sh

Docs baselined: README.md, TODO.md, .mistwood/CHECKLIST.md, .mistwood/PRODUCTIZE.md

Pushed to GitHub, verified

Evennia prod up; ports fixed (4001 → 4005); server boots clean.

Custom ping command implemented and verified.

Hot-reload @rld wired (Account cmdset).

Repaired default_cmdsets.py (removed heredoc artifacts).

VS Code tasks for prod: start/stop/restart/status/tail/open-web.

todo-ack.sh + review-ack.sh (incl. “quick” variant).

Repo-local keybinding (Ctrl+Alt+Shift+K for review-ack).

GitHub issue template (.github/ISSUE_TEMPLATE/task.md).

Import-time profiling task (dev:profile reload).

Telemetry FastAPI app scaffold; /metrics verified.

/status page rendering UP/DOWN for target ports.

tools/health.sh (nice quick LED readout).

Multi-root VS Code workspace showing mistwood + mistwood-dev.

File flow helpers: ops:list files and ops:show file tasks.

Keybinding sync script works (you pushed & pulled successfully).

Stopped old mistwood instance and moved work to mistwood-dev. 100%

Fixed twistd shebang to point at the dev venv. 100%

VS Code dev tasks (dev:start/stop/restart/status/tail/open web) in place. 100%

Added VS Code task docs:update map (calls the generator once it’s real). 100%

Evennia dev server boots cleanly; web at :4105 serves. 100%

Naming — memory system “Grove”; participants “Grovers”. (100%)

hotkeys created:
Hotkeys & quick actions you already have

Ctrl+Alt+Shift+K → todo:review-ack:quick (currently fails due to quoting — see fix below).

Dev server tasks (you added keybindings 1–6): dev:start, dev:stop, dev:restart, dev:status, dev:tail logs, dev:open web.

Health — ops:health.

Show tree/file — ops:list files, ops:show file (prompts for path).

Telemetry — telemetry:start (background) and “open dashboard/status” tasks (if added).

Telemetry UI /status (port 5055) running and auto-refreshing; shows PROD up, DEV down.

Telemetry server scaffold + /metrics endpoint stub in place.

Health check script (tools/health.sh) working; shows 400x up, 410x down.

Review/ack tooling (tools/review-ack.sh, tools/todo-ack.sh) wired; VS Code task todo:review-ack:quick present.

VS Code workspace created and in use (“MISTWOOD-WORKSPACE”); task suite for dev ops present (dev:start/stop/restart/status/tail/open web).

WSL interop enabled (/etc/wsl.conf) and verified via powershell.exe OK.

GitHub CLI authenticated (gh auth status OK; protocol SSH).

Docs skeleton in docs/ established, including MAP.md mind-map and foundational guides.

Evennia dev stack runs (portal + server).

Listening: 4100 (telnet), 4101 (web-proxy), 4105 (webserver), 4106 (AMP).

Prod stack stopped/clean.

Twisted pinned to a compatible version (24.11.0) with Evennia 5.0.1.

Web UI loads at http://localhost:4105 (confirmed “first webpage loaded perfectly”).

VS Code tasks in place: dev:start/stop/restart/status/tail, dev:open web, docs:open map, and added docs:update map.

docs/MAP.md mindmap scaffold created (with Quick Links placeholder).

System Node.js + npm installed; Python websocket-client installed.

WEBSOCKET_CLIENT_PORT flipped to 4102 and verified in logs/ss.

WebSocket smoke (ws_smoke.py) connects.

tools/gen_map.py in place and working (Quick Links now populate).

tools/gen_timeline.py runs and writes docs/TIMELINE.md.

Docs created: COMMUNITY-GUIDELINES.md, MEMORY.md, AI-WORKFLOW.md, PSYCHOLOGY-DESIGN.md.

update-map GitHub Action present in both repos.

Fix Evennia port settings format (both trees) → WEBSERVER_PORTS now list-of-tuples.

Silence gh ... 404 spam in tools/gen_map.py.

Web pages scaffolded: /ai/ (content present), /dashboard/ (reads ports from logs), /timelapse/ (page + speed slider UI).

mmdc installed via Node 22 (mmdc -V prints 11.9.0).

gen_map.py runs and updates docs/MAP.md quick links.

Port settings fixed (WEBSERVER_PORTS tuples).

gen_map.py quieted; MAP.md quick links update working.

/ai/, /dashboard/, /timelapse/ scaffolded; speed slider added.

mmdc working; gen_timeline.py writes TIMELINE.mmd.

Telnet (4100) reachable; login via Mushclient + @reloadcmds works.

Prod/dev port split:

prod (4005→4001, websocket 4002)

dev (4105→4101, telnet 4100, AMP 4106).

tools/timelapse.sh rewritten for TIMELINE-{timeline,mindmap}.mmd; timeline video renders.

tools/publish_timelapse.sh created; web/static/telemetry/grade.json seeded.

web/website/templates/website/{ai_onboarding,dashboard}.html exist and render once routing imports succeed.

Basic CI workflow (.github/workflows/ci.yml) added.

Timelapse: timeline.mp4 renders and is published to web/static/timelapse/ (~32 KB).

Timelapse: mindmap.mp4 now renders (fixed the “width not divisible by 2” issue; output ~32 KB) and is published.

Scripts added + executable: tools/timelapse.sh, tools/publish_timelapse.sh.

Grove telemetry sync: tools/grove_sync.py writes web/static/telemetry/grade.json.

VSCode task: “grove:sync grade” created (.vscode/tasks.json).

Mermaid input cleanup: docs/TIMELINE-*.mmd sanitized and rendered.

Settings: WEBSOCKET_CLIENT_PORTS=[4102] written in both server/conf/settings.py and server/conf/secret_settings.py; verified via a Django settings print.

Branch + PR: chore/ops-docs-telemetry pushed; workflows, docs, and templates committed.

Timelapse build & publish locally

tools/timelapse.sh and tools/publish_timelapse.sh created and run; MP4s exist at web/static/timelapse/ and play ✅

Telemetry grade generation

tools/grove_sync.py executed; web/static/telemetry/grade.json written (grade B+, score 90) ✅

Evennia/GAME port hints

WEBSOCKET_CLIENT_PORTS = [4102] injected into settings, portal/server restart done ✅

Website templates & URLs

web/website/templates/website/{timelapse.html, ai_onboarding.html, dashboard.html} ✅

web/website/urls.py with three routes ✅

GitHub CLI auth (gh auth login) ✅

Naming decisions

Keep Canopy (orchestrator), adopt Kaliana Loop (the agile swing), retain Grove ✅

Added pages/templates, workflow, timelapse tools; branch pushed & PR path available

VS Code tasks added; timelapse mp4s generated locally

TRAILGUIDE.md created (needs tidy)

Web endpoints load (200 OK): /timelapse/, /dashboard/.
(Confirmed by your curl returning HTTP/1.1 200 OK.)

Django import fix: removed web/website/views/ package; single views.py now used.

Settings safety: appended INSTALLED_APPS += ["web.website"] without clobbering defaults.

Evennia running cleanly (manual start shows correct ports 4100/4101/4105/4106, 4002).

Timelapse pipeline (local): MP4s built and published to web/static/timelapse/.

GitHub Actions workflow: timelapse-and-telemetry.yml builds timelapse, generates telemetry, commits assets.

Repo variables set: DEPLOY_HOST, DEPLOY_USER, DEPLOY_DIR.

Trailguide created & improved; ZIPLINE doc rename completed.

Blog-style explainer for Grove / Canopy / Kaliana Loop / Trailguide produced.

Evennia dev server starts/restarts cleanly; /timelapse + /dashboard return 200.

tools/ev.sh points to the right venv; start/restart work.

Self-hosted runner registered & systemd service running.

TODO backlog seeded and getting updates (we’ll automate it every block).

site routes & views committed (timelapse/dashboard/ai-onboarding/licensing) and pushed.

timelapse page responds 200 OK at :4105/timelapse/.

telemetry writer: tools/grove_sync.py created; writes web/static/telemetry/grade.json; history/EWMA/letter grade implemented.

Caddyfile drafted: consolidated and namespaced for dev/prod; static and /ws handlers defined.

prod venv created and Evennia 5.0.1 installed.

CI workflow file (.github/workflows/timelapse-and-telemetry.yml) added/updated and pushed.

/etc/hosts entries for local domains
Added: mistwood.localhost, dev.mistwood.localhost

Caddyfile validates & service restarts
Commands: sudo caddy fmt --overwrite /etc/caddy/Caddyfile → sudo caddy validate --config /etc/caddy/Caddyfile (Valid) → sudo systemctl restart caddy

Project-level URLConf simplified & health check added
File: /home/atlantis/dev/mistwood-dev/web/urls.py now includes include("web.website.urls") + healthz

Template placeholders exist for pages
Created: /web/templates/website/{dashboard,how_we_license,ai_onboarding,timelapse}.html

Evennia pyc cleanup (to address “bad marshal data”)
Ran: find . -name '__pycache__' -type d -exec rm -rf {} + -o -name '*.pyc' -delete in both dev & prod trees

Third-party notices generator and file
Added: tools/gen_3rd_party.py; generated THIRD_PARTY_NOTICES.md (note: commit is still blocked by pre-commit hook — see above)

Ports respond directly on DEV HTTP server
curl -I http://127.0.0.1:4105/timelapse/ ⇒ 200 OK (so Evennia’s web stack is serving; the failing pages are specific routes/templates)

Evennia (DEV) boots and serves — evennia start OK; ports up (4115 web, 4111 internal web, 4110 telnet, 4002 websocket as currently running). 100%

Basic website wiring (DEV) — web/urls.py, web/website/urls.py, views.py in place; /timelapse/ returns 200. 100%

Health endpoint (DEV) — /healthz added and reachable through the app. 100%

Editor keybindings sync system — tools/editor-sync.py + user systemd timer installed and running; logs show periodic sync. 100%

Caddyfile syntax fixed & service running — caddy fmt/validate passes; systemctl restart caddy OK. 100%

Third-party notices generator — tools/gen_3rd_party.py created and ran; THIRD_PARTY_NOTICES.md written locally. 100% (file exists; commit still pending — see below)

Rotated GitHub token & repo secret set — new token created; Actions secret GH_PAT set via CLI; gh auth status OK. 100%

DEV Evennia app up — evennia start OK; /timelapse/ returns 200; Django app (web/website) wired. 100%

Editor sync service — tools/editor-sync.py + systemd timer installed; logs show hourly runs and manual trigger OK. 100%

Keybindings & tasks expanded — repo editor/vscode/keybindings.json updated; .vscode/tasks.json now includes evennia:* tasks; tools/ev.sh rewritten to correct paths. 100%

Nested repo cleanup — removed tracked mistwood/ from index, added to .gitignore, then deleted the directory. 100%

CI dispatch unblocked (branch) — added workflow_dispatch stub on chore/try-ci and successfully dispatched with gh workflow run. 100%

Utility scripts added — tools/grove_sync.py (fixed), tools/snapshot.sh, tools/hotkeys_report.py created. 100%

Dev site (Caddy) returns 200 — http://dev.mistwood.localhost/timelapse/ OK.

Hotkeys + tasks synced — Ctrl+Shift+R now runs reload; Linux & Windows keybinding files corrected; tools/editor-sync.py working.

Caddy site header checker — tools/verify_caddy_hosts.py in place; confirms http:// scheme on prod site files.

“Evennia → Mistwood” pass — Applied to 99 files with legal files excluded; tool retained THIRD_PARTY_NOTICES.md.

Snapshot & hotkeys docs — tools/snapshot.sh generated docs/SNAPSHOT.txt; tools/hotkeys_report.py wrote web/static/docs/hotkeys.md.

PR opened to put workflow on main — ci/workflow-on-main is up; PR #1 created.

Prod settings debug — _settings_debug.txt proves current values being loaded.

Both servers up:

DEV: telnet 4110, web 4115→4111, ws 4002.

PROD: telnet 4100, web 4105→4101, ws disabled.
curl -I http://mistwood.localhost/healthz → 200 ✅

Caddy fixes: all site blocks explicitly http://…; validation/reload OK; host-verifier script added.

Hotkeys: Linux and Windows keybindings synced; Ctrl+Shift+R works; full set functional again; hotkeys doc generated.

Evennia→Mistwood rename applied (99 files), imports/legal left intact (with the caveat above).

Pre-commit installed (hook now noisy when missing config, but installed).

SUDO_EDITOR=“code --wait” set; sudoedit friction removed.

Snapshot/Runbook/Hotkeys outputs refreshed and committed (on branch).

Ports/Caddy health: 100%

Hotkeys working: 100%


