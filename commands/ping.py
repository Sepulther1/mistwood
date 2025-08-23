from evennia import Command

class CmdPing(Command):
    """
    ping — quick connectivity test
    Usage: ping
    """
    key = "ping"
    locks = "cmd:all()"

    def func(self):
        self.caller.msg("|gPONG from Evennia!|n")
