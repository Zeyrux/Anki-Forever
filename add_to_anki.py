import os
import psutil
from pathlib import Path
from pathlib import Path
from shutil import copy

PATH_ANKI_INIT = Path(
    os.path.expanduser("~"), "AppData\\Roaming\\Anki2\\addons21\\myaddon\\__init__.py"
)
PATH_PROJECT_INIT = "__init__.py"
PATH_ANKI_FOREVER = Path(
    os.path.expanduser("~"),
    "AppData\\Roaming\\Anki2\\addons21\\myaddon\\AnkiForever.py",
)
PATH_PROJECT_FOREVER = "AnkiForever.py"

for proc in psutil.process_iter():
    proc_info = proc.as_dict(["exe"])
    if proc_info["exe"] == "C:\\Program Files\\Anki\\anki.exe":
        proc.kill()

if Path(PATH_ANKI_INIT).exists():
    Path(PATH_ANKI_INIT).unlink()
copy(PATH_PROJECT_INIT, PATH_ANKI_INIT)
if Path(PATH_ANKI_FOREVER).exists():
    Path(PATH_ANKI_FOREVER).unlink()
copy(PATH_PROJECT_FOREVER, PATH_ANKI_FOREVER)

os.startfile(Path("C:\\Program Files\\Anki\\anki.exe"))
