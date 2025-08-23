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
