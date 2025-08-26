from django.shortcuts import render

def timelapse(request):
    return render(request, "website/timelapse.html")

def ai_onboarding(request):
    return render(request, "website/ai_onboarding.html")

def dashboard(request):
    # Fill with real telemetry later; stub now so the page loads.
    ctx = {"telnet": None, "web": None, "telemetry": {}}
    return render(request, "website/dashboard.html", ctx)
