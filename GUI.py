from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QProgressBar

from downloader import Downloader


app = QApplication([])

# a input field for the url and a button to start the download
# a label to show the progress of the download

window = QWidget()
window.setWindowTitle("Youtube Downloader")
window.resize(500, 500)


url_label = QLabel("URL", window)
url_label.move(10, 10)

url_input = QLineEdit(window)
url_input.move(10, 30)

path_label = QLabel("Path", window)
path_label.move(10, 60)

path_input = QLineEdit(window)
path_input.move(10, 80)

progress_label = QLabel("Progress", window)
progress_label.move(10, 110)

progress_bar = QProgressBar(window)
progress_bar.move(10, 130)

start_button = QPushButton("Start", window)
start_button.move(10, 160)

def start_download():
    url = url_input.text()
    path = path_input.text()
    downloader = Downloader(url, path)
    downloader.download()

start_button.clicked.connect(start_download)

window.show()
app.exec()

