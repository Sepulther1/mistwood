#!/usr/bin/env bash
set -euo pipefail
check() { ss -ltn '( sport = :'$1' )' | grep -q :$1 && echo "🟢 $2:$1" || echo "🔴 $2:$1"; }
echo "=== Health @ $(date '+%F %T %Z') ==="
check 4000 prod-telnet
check 4001 prod-web-proxy
check 4002 prod-websocket
check 4005 prod-web
check 4100 dev-telnet
check 4101 dev-web-proxy
check 4102 dev-websocket
check 4105 dev-web
# telemetry (single port)
ss -ltn '( sport = :5055 )' | grep -q :5055 && echo "🟢 telemetry:5055" || echo "🟡 telemetry:5055 (off)"
