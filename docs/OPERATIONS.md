# Operations Runbook

## Ports (dev)
- Telnet: **4100**
- Web proxy (external): **4105**
- Web server (internal): **4101**
- Websocket (webclient): **4102**
- AMP (portal↔server): **4106**

## Start / Stop / Reload
```bash
cd /home/atlantis/dev/mistwood-dev-dev && source .venv/bin/activate
python -m evennia -l start      # start & tail logs
python -m evennia -l reload     # hot reload
pkill -f twistd || true         # hard stop
