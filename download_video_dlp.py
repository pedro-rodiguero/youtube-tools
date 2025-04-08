import yt_dlp


def download_video_with_audio(url, path):
    ydl_opts = {
        "format": "bestvideo[height<=2160]+bestaudio/best",  # Ensures 4K (2160p) or lower if 4K is unavailable
        "merge_output_format": "mp4",  # Ensures the output is in MP4 format
        "outtmpl": f"{path}/%(title)s.%(ext)s",  # Output file template
        "postprocessor_args": [
            "-ss",
            "00:00:00",  # Start time (HH:MM:SS)
            "-t",
            "00:05:00",  # Duration (HH:MM:SS) - 5 minutes
        ],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# Use the function
download_video_with_audio(
    "https://www.youtube.com/watch?v=kSZddHca0ME", "/home/pedro/Desktop/Igreja/Pascoa"
)
