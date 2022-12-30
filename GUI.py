from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QProgressBar, QComboBox, QFileDialog

from downloader import Downloader


class DownloadWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Youtube Downloader")
        self.resize(500, 500)
        self.path_input = ""
        self.setup_ui()


    def setup_ui(self):
        self.url_label = QLabel("URL", self)
        self.url_label.move(10, 10)

        self.url_input = QLineEdit(self)
        self.url_input.move(10, 30)

        self.path_label = QLabel("Path", self)
        self.path_label.move(10, 60)

        # browse button
        self.path_input = QLineEdit(self)
        self.path_input.move(10, 80)

        self.browse_button = QPushButton("Browse", self)
        self.browse_button.move(10, 110)
        self.browse_button.clicked.connect(self.browse)





        self.quality_label = QLabel("Quality", self)
        self.quality_label.move(10, 140)

        self.quality_input = QComboBox(self)
        self.quality_input.addItems(["720p", "480p", "360p", "240p", "144p"])
        self.quality_input.move(10, 160)

        self.download_button = QPushButton("Download", self)
        self.download_button.move(10, 190)
        self.download_button.clicked.connect(self.start_download)







    def browse(self):
        path = QFileDialog.getExistingDirectory(self, "Select Download Directory")
        self.path_input.setText(path)


    def start_download(self):
        print(self.path_input.text(), self.url_input.text(), self.quality_input.currentText())
        url = self.url_input.text()
        path = self.path_input.text()
        quality = self.quality_input.currentText()
        downloader = Downloader(url, path, quality)
        downloader.download()
