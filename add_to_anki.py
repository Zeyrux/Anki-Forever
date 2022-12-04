import os
import psutil
from pathlib import Path
from pathlib import Path
from shutil import copy

PATH_ANKI = Path(os.path.expanduser("~"), "AppData\\Roaming\\Anki2\\addons21\\myaddon\\__init__.py")
PATH_PROJECT = "__init__.py"

for proc in psutil.process_iter():
    proc_info = proc.as_dict(["exe"])
    if proc_info["exe"] == "C:\\Program Files\\Anki\\anki.exe":
        proc.kill()
if Path(PATH_ANKI).exists():
    Path(PATH_ANKI).unlink()
copy(PATH_PROJECT, PATH_ANKI)
os.startfile(Path("C:\\Program Files\\Anki\\anki.exe"))