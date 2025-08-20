from evennia import CmdSet
from commands.reflection import CmdReflect, CmdJournal, CmdMentor

"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""

from evennia.objects.objects import DefaultCharacter

from .objects import ObjectParent


class Character(ObjectParent, DefaultCharacter):
    """
    The Character just re-implements some of the Object's methods and hooks
    to represent a Character entity in-game.

    See mygame/typeclasses/objects.py for a list of
    properties and methods available on all Object child classes like this.

    """

    pass
# --- Reflection commands cmdset hook ---
from evennia import CmdSet
from commands.reflection import CmdReflect, CmdJournal

class ReflectionCmdSet(CmdSet):
    """
    Lightweight personal-growth commands available to all Characters.
    """
    key = "ReflectionCmdSet"

    def at_cmdset_creation(self):
        self.add(CmdReflect())
        self.add(CmdJournal())

# Extend the Character to include our commands
# If you already override at_cmdset, merge the 'add' line into it.
def at_cmdset(self, **kwargs):
    super(Character, self).at_cmdset(**kwargs)  # type: ignore[name-defined]
    self.cmdset.add(ReflectionCmdSet)
# End reflection hook
class ReflectionCmdSet(CmdSet):
    key = "ReflectionCmdSet"
    def at_cmdset_creation(self):
        self.add(CmdReflect())
        self.add(CmdJournal())
        self.add(CmdMentor())
class ReflectionCmdSet(CmdSet):
    """
    Lightweight personal-growth commands available to all Characters.
    """
    key = "ReflectionCmdSet"

    def at_cmdset_creation(self):
        self.add(CmdReflect())
        self.add(CmdJournal())
        self.add(CmdMentor())