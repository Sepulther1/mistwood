from evennia import default_cmds
from .ping import CmdPing
from .devtools import CmdReloadCommands

class CharacterCmdSet(default_cmds.CharacterCmdSet):
    key = "DefaultCharacter"
    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        self.add(CmdPing())

class AccountCmdSet(default_cmds.AccountCmdSet):
    key = "DefaultAccount"
    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        self.add(CmdPing())
        self.add(CmdReloadCommands())  # exposes @rld to builders/admins

class UnloggedinCmdSet(default_cmds.UnloggedinCmdSet):
    key = "DefaultUnloggedin"
    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        self.add(CmdPing())

class SessionCmdSet(default_cmds.SessionCmdSet):
    key = "DefaultSession"
    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        # keep empty unless you want session-level commands
