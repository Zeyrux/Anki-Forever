from aqt import gui_hooks, mw
from aqt.utils import showInfo


class AddOn:
    def __init__(self, important_decks: list[str]) -> None:
        self.started = False
        self.important_decks = [deck.replace("::", "") for deck in important_decks]

    def start(self) -> None:
        self.dids = []
        self.started = True
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
        else:
            showInfo("DO SOME WORK LAZY DUDE!")


class App:
    def __init__(self, important_decks: list[str]) -> None:
        self.add_on = AddOn(important_decks)

    def start(self):
        if not self.add_on.started:
            self.add_on.start()
