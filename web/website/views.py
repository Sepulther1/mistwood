from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, "website/dashboard.html", {})
