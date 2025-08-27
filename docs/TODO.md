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
- [ ] Audit VS Code tasks and tools/ev.sh to use /home/atlantis/dev/mistwood-dev/.venv (no references to /home/atlantis/dev/mistwood).
- [ ] One-time DEPLOY_KEY fingerprint check in CI (remove after verifying).
- [ ] Clean workflow: single job, runs-on: self-hosted; remove ubuntu-latest duplicate.
- [ ] Blue/green layout: prod vs dev instances on separate ports; proxy cut-over with Caddy/Nginx.
- [ ] Branding: replace Evennia name where appropriate (keep copyright/attribution).
- [ ] Website pass: ensure /dashboard and pages show telemetry, grades, links, docs.
- [ ] Legal: draft OSS/proprietary split, license files, attribution, and trademark plan; add “How we license” page.
- [ ] Device matrix: test telnet, webclient, websocket; document ports and connection options.
- [ ] Make deploy step local on self-hosted runner (no SSH).
- [ ] Add real checks to grove_sync (GitHub checks, port probes, artifact freshness).
- [ ] Blue/green prod vs dev; Caddy cut-overs.
- [ ] “How we license Mistwood” page & docs attribution for Evennia.
- [ ] Public mirror (or confirm repo stays public) for AI audits.
- [ ] Create GH labels (chore, infra, legal, docs) with gh CLI (needs repo scope).
- [ ] Device matrix (telnet, webclient, websocket) and connection docs.
- [ ] Convert deploy to local (done), remove SSH from workflow.
- [x] Helpers audit; fix site routes; switch workflow to local reload; add fingerprint input; Caddy fixed.
