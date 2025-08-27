r"""
Evennia settings file.

The available options are found in the default settings file found
here:

https://www.evennia.com/docs/latest/Setup/Settings-Default.html

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "mistwood-dev"


######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")




# --- Mistwood (dev) ports ---
TELNET_ENABLED = True
TELNET_INTERFACES = ["0.0.0.0"]
TELNET_PORTS = [4100]

# Pairs: (proxy_port, server_port)
WEBSERVER_PORTS = [(4105, 4101)]

# Websocket client (list of ints)


AMP_PORT = 4106
# Dev override (final):

# Final dev override
WEBSOCKET_CLIENT_PORTS = [4102]

try:
    INSTALLED_APPS
except NameError:
    INSTALLED_APPS = []
INSTALLED_APPS += ["web.website"]