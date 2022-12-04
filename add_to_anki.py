from pathlib import Path
from shutil import copy

PATH_ANKI = "C:\\Users\\HP\\AppData\\Roaming\\Anki2\\addons21\\myaddon\\__init__.py"
PATH_PROJECT = "C:\\Zeyrux\\Python\\Anki-forever\\__init__.py"

if Path(PATH_ANKI).exists():
    Path(PATH_ANKI).unlink()
copy(PATH_PROJECT, PATH_ANKI)
