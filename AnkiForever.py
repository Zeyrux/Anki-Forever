import sys
import psutil
import base64

from PyQt6.QtWidgets import QApplication, QMainWindow


STYLE_APP = "Fusion"


# CHECKS = ["exe", "name"]
# BLACKLIST = {
#     "exe": [
#         "C:\\Program Files\\WindowsApps\\Microsoft.Office.OneNote_16001.14326.21146.0_x64__8wekyb3d8bbwe\\onenoteim.exe"
#     ],
#     "name": ["onenoteim.exe"],
# }

# for proc in psutil.process_iter():
#     proc_info = proc.as_dict(CHECKS)
#     for check in CHECKS:
#         if proc_info[check] in BLACKLIST[check]:
#             proc.kill()

# auf anki plugin gehen (eher nicht PyQt6 App)
class App(QMainWindow):
    def __init__(self):
        super().__init__()


def create_app():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.setStyle(STYLE_APP)
    app.exec()


create_app()
