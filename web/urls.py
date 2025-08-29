from django.urls import include, path
from evennia.web.urls import urlpatterns as evennia_default_urlpatterns

# Only our site pages here; Evennia's defaults bring in webclient/admin.
urlpatterns = [
    path("", include("web.website.urls")),
] + evennia_default_urlpatterns
