from django.shortcuts import render

def _r(request, name, ctx=None):
    return render(request, f"website/{name}.html", ctx or {})

def timelapse(request):      return _r(request, "timelapse")
def dashboard(request):      return _r(request, "dashboard")
def ai_onboarding(request):  return _r(request, "ai_onboarding")
def how_we_license(request): return _r(request, "how_we_license")
