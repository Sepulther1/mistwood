<<<<<<< HEAD
# /home/atlantis/dev/mistwood-dev-dev/commands/devtools.py
from evennia import Command
import importlib

class CmdReloadCommands(Command):
    """
    reloadcmds

    Reload project command modules (dev helper).
    """
    key = "reloadcmds"
    locks = "cmd:perm(Developer)"

    def func(self):
        try:
            import commands.default_cmdsets as default_cmdsets
            import commands.devtools as devtools  # this file
            importlib.reload(default_cmdsets)
            importlib.reload(devtools)
            self.caller.msg("|gReloaded command modules.|n")
        except Exception as e:
            self.caller.msg(f"|rError: {e}|n")
=======
from evennia import Command
import importlib, sys

class CmdReloadCommands(Command):
    """
    @rld — Hot-reload all modules under commands.*
    Usage: @rld
    """
    key = "@rld"
    locks = "cmd:perm(Builder) or perm(Admin)"

    def func(self):
        try:
            __import__("commands")
            for name, mod in list(sys.modules.items()):
                if name == "commands" or name.startswith("commands."):
                    importlib.reload(mod)
            try:
                self.caller.cmdset.update()
            except Exception:
                pass
            self.caller.msg("|gReloaded commands.*|n")
        except Exception as e:
            self.caller.msg(f"|rError: {e}|n")
>>>>>>> origin/main
