from evennia import Command

class CmdPing(Command):
    """
    ping

    Usage:
      ping

Replies with a simple message so you can verify that command wiring works.
    """
    key = "ping"
    locks = "cmd:all()"
    help_category = "General"

    def func(self):
        self.caller.msg("PONG from Mistwood!")
