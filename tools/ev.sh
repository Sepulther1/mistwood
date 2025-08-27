#!/usr/bin/env bash
set -euo pipefail
cd /home/atlantis/dev/mistwood-dev
source .venv/bin/activate

case "${1:-}" in
  start)   python -m evennia start ;;
  stop)    python -m evennia stop ;;
  restart) python -m evennia restart ;;
  reload)  python -m evennia -l reload ;;   # <— reload
  status)  python -m evennia status ;;
  tail)    python -m evennia -l ;;
  tail-stop) killall -q -INT tail || true ;;
  open-web) xdg-open http://127.0.0.1:4105/ || true ;;
  *) echo "Usage: tools/ev.sh {start|stop|restart|reload|status|tail|tail-stop|open-web}" ; exit 2 ;;
esac
