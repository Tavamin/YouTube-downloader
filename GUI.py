from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QProgressBar

from downloader import Downloader


class DownloadWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Youtube Downloader")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        self.url_label = QLabel("URL", self)
        self.url_label.move(10, 10)

        self.url_input = QLineEdit(self)
        self.url_input.move(10, 30)

        self.path_label = QLabel("Path", self)
        self.path_label.move(10, 60)

        self.path_input = QLineEdit(self)
        self.path_input.move(10, 80)

        self.progress_label = QLabel("Progress", self)
        self.progress_label.move(10, 110)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.move(10, 130)

        self.start_button = QPushButton("Start", self)
        self.start_button.move(10, 160)

        self.start_button.clicked.connect(self.start_download)

    def start_download(self):
        url = self.url_input.text()
        path = self.path_input.text()
        downloader = Downloader(url, path)
        downloader.download()
