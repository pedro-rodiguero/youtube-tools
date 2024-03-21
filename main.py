from pytube import YouTube


def download_video(url, path):
    yt = YouTube(url)
    yt.streams.get_highest_resolution().download(path)


# Use the function
download_video(
    "https://www.youtube.com/watch?v=5p_SuO96Jd4", "/home/pedro/Desktop/Igreja/Pascoa"
)
