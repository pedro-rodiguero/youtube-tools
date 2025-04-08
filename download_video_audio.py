from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from pydub import AudioSegment
import os
import sys
from urllib.error import HTTPError


def progress_function(stream, chunk, bytes_remaining):
    # Implement your progress function here
    pass


def download_video_as_audio(url, path):
    try:
        yt = YouTube(url, on_progress_callback=progress_function)
        video = yt.streams.filter(progressive=True, file_extension="mp4").first()
        if video:
            video_file = video.download(path)
            audio_file_without_ext = os.path.splitext(video_file)[0]
            audio_file_mp3 = f"{audio_file_without_ext}.mp3"

            # Convert mp4 video to mp3 audio
            audio = AudioSegment.from_file(video_file, format="mp4")
            audio.export(audio_file_mp3, format="mp3")
            # Remove the original mp4 file
            os.remove(video_file)
        else:
            print("No video stream available with the specified format.")
    except VideoUnavailable:
        print(f"Video {url} is unavailable.")
    except HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Use the function
download_video_as_audio(
    "https://www.youtube.com/watch?v=gTRFVMkMajw", "/home/pedro/Desktop/Igreja/Pascoa"
)
