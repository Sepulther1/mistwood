from django.urls import path
from . import views

urlpatterns = [
    path("timelapse/", views.timelapse, name="timelapse"),
    path("ai-onboarding/", views.ai_onboarding, name="ai_onboarding"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
