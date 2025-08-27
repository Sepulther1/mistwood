# /home/atlantis/dev/mistwood-dev/commands/devtools.py
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