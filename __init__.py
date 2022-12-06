from aqt import gui_hooks
from .AnkiForever import App

app = App()


gui_hooks.sync_will_start.append(app.start)
