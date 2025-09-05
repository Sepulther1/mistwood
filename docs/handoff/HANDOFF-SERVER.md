# Mistwood/Grove Server & Adapters (snapshot)

## Endpoints
- /health, /about, /grove/chat

## Core docs

## Running (dev)
```bash
cd /home/atlantis/dev/mistwood-dev
PORT=$(p=5110; while ss -ltn | grep -q ":$p "; do p=$((p+1)); done; echo $p)
uvicorn mistwood_server.app:app --host 127.0.0.1 --port "$PORT" --reload
```

## Telnet dev
- tools/run_telnet_dev.sh (port 4010)

## IRC bridge
- tools/run_irc_bridge.sh (uses ~/.mistwood/irc_bridge.last.json)
