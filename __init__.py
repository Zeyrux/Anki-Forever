from aqt import gui_hooks
from .AnkiForever import App

IMPORTANT_DECK_PATH = [
    "ENG::Vocab::English LK::Eng 11 aims and ambitious",
    "ENG::Vocab::English LK::ENG 11 gender issues",
]

app = App(IMPORTANT_DECK_PATH)


gui_hooks.sync_will_start.append(app.start)
