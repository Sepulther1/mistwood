from evennia import Command
from evennia.utils.utils import datetime_format
from datetime import datetime

def _now():
    # Compact, human-readable timestamp
    return datetime_format(datetime.utcnow())

class CmdReflect(Command):
    """
    reflect <text>
    
    Add a timestamped reflection entry to your personal journal.
    """
    key = "reflect"
    locks = "cmd:all()"

    def parse(self):
        self.text = self.args.strip()

    def func(self):
        if not self.text:
            self.caller.msg("|yUsage:|n reflect <your thoughts>")
            return
        journal = (self.caller.db.journal or [])
        entry = {"t": _now(), "text": self.text}
        journal.append(entry)
        self.caller.db.journal = journal
        self.caller.msg(f"|gSaved reflection|n at |w{entry['t']}|n.")

class CmdJournal(Command):
    """
    journal [N]
    
    Show the last N reflection entries (default 10).
    """
    key = "journal"
    locks = "cmd:all()"

    def parse(self):
        try:
            self.n = int(self.args.strip()) if self.args.strip() else 10
        except ValueError:
            self.n = 10

    def func(self):
        journal = (self.caller.db.journal or [])
        if not journal:
            self.caller.msg("|yNo journal entries yet. Try:|n reflect I felt focused today")
            return
        tail = journal[-self.n:]
        lines = []
        for e in tail:
            lines.append(f"|w{e['t']}|n — {e['text']}")
        body = "\n".join(lines)
        self.caller.msg(f"|cYour last {len(tail)} reflections:|n\n{body}")
class CmdMentor(Command):
    """
    mentor on|off  — opt-in to periodic mentor prompts.
    """
    key = "mentor"
    locks = "cmd:all()"

    def parse(self):
        self.arg = (self.args or "").strip().lower()

    def func(self):
        if self.arg not in {"on", "off"}:
            self.caller.msg("|yUsage:|n mentor on|off")
            return
        self.caller.db.mentor_optin = (self.arg == "on")
        state = "enabled" if self.caller.db.mentor_optin else "disabled"
        self.caller.msg(f"|gMentor prompts {state}.|n")