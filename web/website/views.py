import urllib.request, socket
from django.shortcuts import render

def _r(request, name, ctx=None):
    return render(request, f"website/{name}.html", ctx or {})

def _ok(url, timeout=1.5):
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.status == 200
    except Exception:
        return False

def dashboard(request):
    ctx = {
        "dev_ok":  _ok("http://dev.mistwood.localhost/timelapse/"),
        "prod_ok": _ok("http://mistwood.localhost/healthz"),
        "ports": {
            "dev":  {"telnet": 4110, "web": "4115→4111", "ws": 4002},
            "prod": {"telnet": 4100, "web": "4105→4101", "ws": "disabled"},
        },
    }
    return render(request, "website/dashboard.html", ctx)

def timelapse(request):      return _r(request, "timelapse")
def dashboard(request):      return _r(request, "dashboard")
def ai_onboarding(request):  return _r(request, "ai_onboarding")
def how_we_license(request): return _r(request, "how_we_license")
