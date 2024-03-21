import subprocess


def quadruple_frames(input_path, output_path):
    command = [
        "ffmpeg",
        "-i",
        input_path,
        "-filter:v",
        "minterpolate='mi_mode=mci:mc_mode=aobmc:vsbmc=1:fps=120'",
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
quadruple_frames(
    "path/to/file",
    "path/to/file",
)
