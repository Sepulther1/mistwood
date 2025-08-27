from django.urls import include, path
from evennia.web.urls import urlpatterns as evennia_default_urlpatterns

urlpatterns = [
    path("", include("web.website.urls")),          # website (our pages live here)
    path("webclient/", include("web.webclient.urls")),
    path("admin/", include("web.admin.urls")),
        path("timelapse/", views.timelapse, name="timelapse"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("ai-onboarding/", views.ai_onboarding, name="ai_onboarding"),
    path("licensing/", views.how_we_license, name="how_we_license"),
] + evennia_default_urlpatterns