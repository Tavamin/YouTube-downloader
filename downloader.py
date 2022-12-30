from pytube import YouTube


class Downloader:
    def __init__(self, url, path):
        self.url = url
        self.yt = YouTube(url)
        self.stream = self.yt.streams.first()
        self.path = path


    def download(self):
        try:
            self.stream.download(self.path)

        except Exception as e:
            print(e)


