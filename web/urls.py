from django.urls import include, path
from evennia.web.urls import urlpatterns as evennia_default_urlpatterns

urlpatterns = [
    path("", include("web.website.urls")),          # our site pages
    path("webclient/", include("web.webclient.urls")),
    path("admin/", include("web.admin.urls")),
] + evennia_default_urlpatterns