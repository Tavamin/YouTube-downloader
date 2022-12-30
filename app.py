from PyQt6.QtWidgets import QApplication

from GUI import DownloadWindow

app = QApplication([])

window = DownloadWindow()
window.show()


if __name__ == "__main__":
    app.exec()
