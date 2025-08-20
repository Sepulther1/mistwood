from evennia import Command

class CmdPing(Command):
    """
    ping

    Usage:
      ping

    Replies with a quick PONG so you can test hot-reload and clients.
    """
    key = "ping"
    locks = "cmd:all()"

    def func(self):
        self.caller.msg("|gPONG from Evennia!|n")
