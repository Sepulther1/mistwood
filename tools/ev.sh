#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

LOG=".vscode/ops.log"
ts(){ date '+%F %T'; }
venv(){ source .venv/bin/activate; }

case "${1:-}" in
  start)       echo "[$(ts)] evennia start"   | tee -a "$LOG"; venv; evennia start   2>&1 | tee -a "$LOG" ;;
  stop)        echo "[$(ts)] evennia stop"    | tee -a "$LOG"; venv; evennia stop    2>&1 | tee -a "$LOG" || true ;;
  restart)     echo "[$(ts)] evennia restart" | tee -a "$LOG"; venv; evennia restart 2>&1 | tee -a "$LOG" ;;
  status)      echo "[$(ts)] evennia status"  | tee -a "$LOG"; venv; evennia status  2>&1 | tee -a "$LOG" ;;
  tail)        echo "[$(ts)] tail logs"       | tee -a "$LOG"; tail -n 200 -F server/logs/server.log ;;
  tail-stop)   echo "[$(ts)] stop logs tail"  | tee -a "$LOG"; pkill -f 'tail .*server/logs/server.log' || true ;;
  force-stop)  echo "[$(ts)] evennia FORCE stop" | tee -a "$LOG"
               venv; evennia stop 2>&1 | tee -a "$LOG" || true
               for f in server/portal.pid server/server.pid; do [ -f "$f" ] && kill -TERM "$(cat "$f")" 2>/dev/null || true; done
               sleep 1
               for f in server/portal.pid server/server.pid; do [ -f "$f" ] && kill -KILL "$(cat "$f")" 2>/dev/null || true; done ;;
  open-web)    if command -v wslview >/dev/null 2>&1; then wslview http://127.0.0.1:4001
               else powershell.exe -NoProfile -Command start http://127.0.0.1:4001; fi ;;
  *) echo "Usage: tools/ev.sh {start|stop|restart|status|tail|tail-stop|force-stop|open-web}" >&2; exit 2 ;;
esac