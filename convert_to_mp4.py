import subprocess


def convert_webm_to_mp4(input_path, output_path):
    command = ["ffmpeg", "-i", input_path, "-q:v", "0", output_path]
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    )

    for line in process.stdout:
        print(line, end="")


# Use the function
convert_webm_to_mp4(
    "/home/pedro/Desktop/Igreja/Pascoa/video.webm",
    "/home/pedro/Desktop/Igreja/Pascoa/video.mp4",
)
