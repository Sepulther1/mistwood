from evennia import default_cmds
<<<<<<< HEAD
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
=======
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
>>>>>>> origin/main
