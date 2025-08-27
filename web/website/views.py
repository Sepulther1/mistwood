from django.shortcuts import render
from django.conf import settings
from pathlib import Path
import re, json

def timelapse(request):
    return render(request, "website/timelapse.html")

def ai_onboarding(request):
    return render(request, "website/ai_onboarding.html")

def dashboard(request):
    root = Path(getattr(settings, "GAME_DIR", Path(".")))
    telnet = web = None

    try:
        portal = root / "server" / "logs" / "portal.log"
        m = re.findall(r"Telnet starting on (\d+)", portal.read_text())
        telnet = m[-1] if m else None
    except Exception:
        pass

    try:
        server = root / "server" / "logs" / "server.log"
        m = re.findall(r"Webserver starting on (\d+)", server.read_text())
        web = m[-1] if m else None
    except Exception:
        pass

    telemetry = {}
    try:
        tpath = root / "web" / "static" / "telemetry" / "grade.json"
        telemetry = json.loads(tpath.read_text())
    except Exception:
        telemetry = {}

    return render(
        request,
        "website/dashboard.html",
        {"telnet": telnet, "web": web, "telemetry": telemetry},
    )
