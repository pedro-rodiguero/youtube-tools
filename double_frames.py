import subprocess


def double_frames(input_path, output_path):
    # Use ffprobe to get the input video's frame rate
    probe_command = [
        "ffprobe",
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=r_frame_rate",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        input_path,
    ]
    process = subprocess.run(
        probe_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    frame_rate = process.stdout.strip()

    # Calculate the doubled frame rate
    try:
        num, den = map(int, frame_rate.split("/"))
        doubled_frame_rate = num / den * 2
    except ValueError:
        print("Error: Unable to determine frame rate.")
        return

    # Use ffmpeg to double the frames
    command = [
        "ffmpeg",
        "-i",
        input_path,
        "-filter:v",
        f"minterpolate='mi_mode=mci:mc_mode=aobmc:vsbmc=1:fps={doubled_frame_rate}'",
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
double_frames(
    "/home/pedro/Desktop/Igreja/Pascoa/video1.mp4",
    "/home/pedro/Desktop/Igreja/Pascoa/video_double.mp4",
)
