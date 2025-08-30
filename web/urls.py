from django.urls import include, path
from django.http import HttpResponse
from evennia.web.urls import urlpatterns as evennia_default_urlpatterns

def healthz(_request):
    return HttpResponse("ok", content_type="text/plain")

urlpatterns = [
    path("", include("web.website.urls")),
    path("healthz", healthz),
] + evennia_default_urlpatterns
