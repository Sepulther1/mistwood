#!/usr/bin/env bash
set -euo pipefail
echo "=== Ports ==="; ss -ltnp | egrep ':(4002|4004|4012|4105|4115|4100|4110)' || true
echo; echo "=== Caddyfile ==="; sed -n '1,60p' /etc/caddy/Caddyfile
echo; echo "=== Sites ==="; head -n1 /etc/caddy/sites/mistwood-prod-*.caddy
echo; echo "=== Dev portal.log tail ==="; tail -n 20 /home/atlantis/dev/mistwood-dev/server/logs/portal.log || true
echo; echo "=== Prod portal.log tail ==="; tail -n 20 /home/atlantis/dev/mistwood-prod/server/logs/portal.log || true
echo; echo "=== Workflows present on main ==="
git fetch origin >/dev/null 2>&1
git ls-remote --heads origin main >/dev/null 2>&1 && \
git show origin/main:.github/workflows/timelapse-and-telemetry.yml >/dev/null 2>&1 && echo "timelapse-and-telemetry ✓" || echo "timelapse-and-telemetry ✗"