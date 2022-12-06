import os
import psutil
from pathlib import Path
from pathlib import Path
from shutil import copy

A_INIT = Path(
    os.path.expanduser("~"), "AppData\\Roaming\\Anki2\\addons21\\myaddon\\__init__.py"
)
P_INIT = "__init__.py"
A_FOREVER = Path(
    os.path.expanduser("~"),
    "AppData\\Roaming\\Anki2\\addons21\\myaddon\\AnkiForever.py",
)
P_FOREVER = "AnkiForever.py"
A_BLACKLIST = Path(
    os.path.expanduser("~"),
    "AppData\\Roaming\\Anki2\\addons21\\myaddon\\blacklist.json",
)
P_BLACKLIST = "blacklist.json"

for proc in psutil.process_iter():
    proc_info = proc.as_dict(["exe"])
    if proc_info["exe"] == "C:\\Program Files\\Anki\\anki.exe":
        proc.kill()

if Path(A_INIT).exists():
    Path(A_INIT).unlink()
copy(P_INIT, A_INIT)
if Path(A_FOREVER).exists():
    Path(A_FOREVER).unlink()
copy(P_FOREVER, A_FOREVER)
if Path(A_BLACKLIST).exists():
    Path(A_BLACKLIST).unlink()
copy(P_BLACKLIST, A_BLACKLIST)

os.startfile(Path("C:\\Program Files\\Anki\\anki.exe"))
