from evennia import default_cmds
from commands.devtools import CmdReloadCommands

class CharacterCmdSet(default_cmds.CharacterCmdSet):
    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        # Add character-only commands here, e.g.:
        # self.add(CmdSomething())

class AccountCmdSet(default_cmds.AccountCmdSet):
    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        self.add(CmdReloadCommands())
        # Add account-level commands here

class UnloggedinCmdSet(default_cmds.UnloggedinCmdSet):
    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        # Add commands available before login here

class SessionCmdSet(default_cmds.SessionCmdSet):
    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        # Add session-level commands here