r"""
Mistwood settings (DEV).
"""
from evennia.settings_default import *

SERVERNAME = "mistwood-dev"

try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")

<<<<<<< HEAD
# --- Ports (DEV) ---
TELNET_ENABLED   = True
TELNET_INTERFACES = ["0.0.0.0"]
TELNET_PORTS     = [4110]
WEBSERVER_PORTS  = [(4115, 4111)]  # http, https
WEBCLIENT_PORTS  = [4012]          # websocket
AMP_PORT         = 4116

# Enable our tiny Django app
try:
    INSTALLED_APPS
except NameError:
    INSTALLED_APPS = []
INSTALLED_APPS += ["web.website"]
=======

TELNET_PORTS = [4000]
WEBSERVER_PORTS = [(4001, 4005)]
WEBSOCKET_CLIENT_PORTS = [4002]
>>>>>>> origin/main
