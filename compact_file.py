import subprocess


def compress_video(input_path, output_path, crf=23):
    command = [
        "ffmpeg",
        "-i",
        input_path,
        "-vcodec",
        "libx264",
        "-crf",
        str(crf),
        output_path,
    ]
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    )

    for line in process.stdout:
        print(line, end="")


# Use the function
compress_video(
    "/home/pedro/Desktop/Igreja/Pascoa/video.webm",
    "/home/pedro/Desktop/Igreja/Pascoa/video.mp4",
)
