from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from collections import deque
from time import time

app = FastAPI()
STATE = {
    "started": time(),
    "popups": deque(maxlen=2000),         # timestamps (s)
    "freezes": deque(maxlen=2000),        # (start,end)
    "variant": "A",
    "enter_to_dom_ms": deque(maxlen=2000) # simple latency samples
}

@app.post("/event")
async def event(req: Request):
    data = await req.json()
    t = time()
    etype = data.get("type")
    if etype == "popup":
        STATE["popups"].append(t)
    elif etype == "freeze":
        STATE["freezes"].append((data.get("start", t), data.get("end", t)))
    elif etype == "variant":
        STATE["variant"] = data.get("value", "A")
    elif etype == "latency":
        ms = float(data.get("ms", 0))
        STATE["enter_to_dom_ms"].append(ms)
    return JSONResponse({"ok": True})

@app.get("/metrics")
def metrics():
    now = time()
    pop5 = [p for p in STATE["popups"] if p >= now - 300]
    tot_freeze = sum(max(0, e - s) for s, e in STATE["freezes"])
    lat = list(STATE["enter_to_dom_ms"])
    avg_lat = round(sum(lat)/len(lat), 1) if lat else 0.0
    return {
        "uptime_s": round(now - STATE["started"]),
        "variant": STATE["variant"],
        "popups_5m": len(pop5),
        "popups_total": len(STATE["popups"]),
        "freeze_total_s": round(tot_freeze, 1),
        "lat_avg_ms": avg_lat,
        "lat_samples": len(lat),
    }

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    return """<!doctype html><meta charset="utf-8">
<title>LagLab Dashboard</title>
<h1>LagLab (local)</h1>
<pre id="out">Loading…</pre>
<script>
async function tick(){
  const r = await fetch('/metrics'); const j = await r.json();
  document.getElementById('out').textContent = JSON.stringify(j, null, 2);
}
setInterval(tick, 5000); tick();
</script>"""