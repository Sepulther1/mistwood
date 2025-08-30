#!/usr/bin/env bash
set -euo pipefail
GAME="/home/atlantis/dev/mistwood-dev"
VENV="$GAME/.venv/bin/activate"

case "${1:-}" in
  start)    cd "$GAME" && source "$VENV" && evennia start ;;
  stop)     cd "$GAME" && source "$VENV" && evennia stop  ;;
  restart)  cd "$GAME" && source "$VENV" && evennia restart ;;
  status)   ss -ltnp | egrep ':(4012|4115|4110)' || true ;;
  logs)     tail -f "$GAME/server/logs/server.log" "$GAME/server/logs/portal.log" ;;
  flog)     pkill -f "tail -f .*server.log" || true ;;
  force-stop) pkill -f 'twistd.*mistwood' || true ;;
  open-web) xdg-open "http://dev.mistwood.localhost" >/dev/null 2>&1 || true ;;
  *)
    echo "Usage: $0 {start|stop|restart|status|logs|flog|force-stop|open-web}"
    exit 1
    ;;
esac