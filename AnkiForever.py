import psutil
from threading import Thread
from json import load
from time import sleep

from aqt import gui_hooks, mw
from aqt.utils import showInfo


BLACKLIST_PATH = "blacklist.json"


class Killer:
    def __init__(self, interval=1):
        self.ival = interval
        self.runs = False
        self.blacklist = load(open(BLACKLIST_PATH, "r"))
        self.thread = Thread(target=self._run, daemon=True)

    def start(self):
        self.runs = True
        self.thread.start()

    def stop(self):
        self.runs = False

    def _run(self):
        while self.runs:
            self._kill()
            sleep(1)

    def _kill(self):
        for proc in psutil.process_iter():
            proc_info = proc.as_dict(["name"])
            for name in self.blacklist:
                if proc_info["name"] == name:
                    proc.kill()


class AddOn:
    def __init__(self, important_decks: list[str]) -> None:
        self.runs = False
        self.killer = Killer()
        self.important_decks = [deck.replace("::", "") for deck in important_decks]

    def start(self) -> None:
        self.dids = []
        self.killer.start()
        self.runs = True
        for deck in self.important_decks:
            self.dids.append(
                mw.col.db.first(f"SELECT id FROM decks WHERE name='{deck}'")[0]
            )
        gui_hooks.overview_did_refresh.append(self.my_func)

    def my_func(self, *args):
        finished = True
        for did in self.dids:
            if (
                mw.col.db.first(
                    f"SELECT COUNT(due) FROM cards WHERE did={did} AND cards.due <= {mw.col.sched.today}"
                )[0]
                != 0
            ):
                finished = False
                break
        if finished:
            showInfo("FINISHED for today")
            self.killer.stop()
        else:
            showInfo("DO SOME WORK LAZY DUDE!")


class App:
    def __init__(self, important_decks: list[str]) -> None:
        self.add_on = AddOn(important_decks)

    def start(self):
        if not self.add_on.runs:
            self.add_on.start()
