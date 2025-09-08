#!/usr/bin/env python3
import sys, time, pathlib
log = pathlib.Path(".vscode/ops.log")
log.parent.mkdir(parents=True, exist_ok=True)
ts = time.strftime("%F %T")
if len(sys.argv) >= 3 and sys.argv[1] in {"start","stop"}:
    log.write_text(log.read_text() + f"{ts} WFB {sys.argv[2]} {sys.argv[1]}\n" if log.exists() else f"{ts} WFB {sys.argv[2]} {sys.argv[1]}\n")
    print(f"{sys.argv[1].upper()} {sys.argv[2]}")
else:
    print("usage: wfb.py [start|stop] <NAME>")
