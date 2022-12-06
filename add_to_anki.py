import os
import psutil
from pathlib import Path
from shutil import copy

# kills current anki process
for proc in psutil.process_iter():
    proc_info = proc.as_dict(["exe"])
    if proc_info["exe"] == "C:\\Program Files\\Anki\\anki.exe":
        proc.kill()

# copy files to anki directory
for path in [
    "AnkiForever.py",
    "__init__.py",
    "blacklist_dirs.json",
    "blacklist_specific.json",
    "decks.json",
]:
    a_path = os.path.join(
        os.path.expanduser("~"), "AppData\\Roaming\\Anki2\\addons21\\myaddon", path
    )
    if Path(a_path).exists():
        Path(a_path).unlink()
    copy(path, a_path)

# starts anki
os.startfile(Path("C:\\Program Files\\Anki\\anki.exe"))
