from pytube import YouTube


class Downloader:
    def __init__(self, url, path, quality="720p"):
        self.url = url
        self.yt = YouTube(url)
        self.quality = quality
        self.stream = self.yt.streams.filter(progressive=True, file_extension='mp4').get_by_resolution(self.quality)
        self.path = path

    def download(self):
        try:
            self.stream.download(self.path)

        except Exception as e:
            print(e)
