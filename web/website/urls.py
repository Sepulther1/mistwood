from django.urls import path
from . import views

urlpatterns = [
    path("timelapse/", views.timelapse, name="timelapse"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("ai-onboarding/", views.ai_onboarding, name="ai_onboarding"),
    path("licensing/", views.how_we_license, name="how_we_license"),
]
