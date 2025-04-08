from pytube import YouTube
import os, sys


def progress_function(stream, chunk, bytes_remaining):
    current = (stream.filesize - bytes_remaining) / stream.filesize
    percent = ("{0:.1f}").format(current * 100)
    progress = int(50 * current)
    sys.stdout.write("\r")
    sys.stdout.write("[%-50s] %s%%" % ("=" * progress, percent))
    sys.stdout.flush()


def download_video(url, path):
    yt = YouTube(url, on_progress_callback=progress_function)
    video = yt.streams.filter(only_video=True, resolution="2160p").first()
    if video:
        video.download(path)


# Use the function
download_video(
    "https://www.youtube.com/watch?v=kSZddHca0ME",
    "/home/pedro/Desktop/Igreja/Pascoa",
)
