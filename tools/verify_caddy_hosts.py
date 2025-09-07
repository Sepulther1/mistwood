#!/usr/bin/env python3
from pathlib import Path
FILES = [
    Path("/etc/caddy/sites/mistwood-prod-4105.caddy"),
    Path("/etc/caddy/sites/mistwood-prod-4106.caddy"),
]
bad = []
for f in FILES:
    line1 = f.read_text().splitlines()[0].strip()
    if not line1.startswith("http://mistwood.localhost"):
        bad.append((f, line1))
if bad:
    print("Fix needed in:")
    for f, l in bad:
        print(f" - {f}  (has: {l!r})  => run: sudo sed -i '1s/^mistwood\\.localhost/http:\\/\\/mistwood.localhost/' {f}")
else:
    print("All Caddy site files have explicit http:// scheme.")