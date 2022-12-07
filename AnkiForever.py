import psutil
import os
import atexit
from pathlib import Path
from threading import Thread
from json import load
from time import sleep

from aqt import gui_hooks, mw
from aqt.utils import showInfo

PATH_ADDON = Path(os.path.expanduser("~"), "AppData\\Roaming\\Anki2\\addons21\\myaddon")
PATH_BLACKLIST_SPECIFIC = Path(PATH_ADDON, "blacklist_specific.json")
PATH_BLACKLIST_DIRS = Path(PATH_ADDON, "blacklist_dirs.json")
PATH_DECKS = Path(PATH_ADDON, "decks.json")
ANKI_PATH = Path("C:\\Program Files\\Anki\\anki.exe")


class Killer:
    def __init__(self, interval=1):
        self.ival = interval
        self.runs = False
        self.blacklist_dirs = [
            path.replace("\\\\", "\\") for path in load(open(PATH_BLACKLIST_DIRS, "r"))
        ]
        self.blacklist_specific = load(open(PATH_BLACKLIST_SPECIFIC, "r"))
        for check in self.blacklist_specific.keys():
            self.blacklist_specific[check] = [
                entry.replace("\\\\", "\\") for entry in self.blacklist_specific[check]
            ]
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
            proc_info = proc.as_dict([*self.blacklist_specific.keys()])
            for check in self.blacklist_specific.keys():
                if proc_info[check] is None:
                    continue
                if proc_info[check] in self.blacklist_specific[check]:
                    proc.kill()
                    return
                for dir in self.blacklist_dirs:
                    if dir in proc_info[check]:
                        proc.kill()
                        return


class AddOn:
    def __init__(self) -> None:
        self.runs = False
        self.killer = Killer()
        self.important_decks = [
            deck.replace("::", "") for deck in load(open(PATH_DECKS, "r"))
        ]

    def start(self) -> None:
        self.dids = []
        self.killer.start()
        self.runs = True
        for deck in self.important_decks:
            self.dids.append(
                mw.col.db.first(f"SELECT id FROM decks WHERE name='{deck}'")[0]
            )
        gui_hooks.overview_did_refresh.append(self.my_func)
        atexit.register(self.start_anki)

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

    def start_anki(self):
        if self.killer.runs:
            os.startfile(ANKI_PATH)


class App:
    def __init__(self) -> None:
        self.add_on = AddOn()

    def start(self):
        if not self.add_on.runs:
            self.add_on.start()
