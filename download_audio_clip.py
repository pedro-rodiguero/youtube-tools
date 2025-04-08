# from pytube import YouTube
# from pydub import AudioSegment
# import os, sys
#
#
# def progress_function(stream, chunk, bytes_remaining):
#     current = (stream.filesize - bytes_remaining) / stream.filesize
#     percent = ("{0:.1f}").format(current * 100)
#     progress = int(50 * current)
#     sys.stdout.write("\r")
#     sys.stdout.write("[%-50s] %s%%" % ("=" * progress, percent))
#     sys.stdout.flush()
#
#
# def download_audio_clip(url, start_time, end_time, path):
#     yt = YouTube(url, on_progress_callback=progress_function)
#     audio = yt.streams.get_audio_only()
#     audio_file = audio.download(path)
#     audio_file_without_ext = os.path.splitext(audio_file)[0]
#     audio_file_mp3 = f"{audio_file_without_ext}.mp3"
#
#     # Convert mp4 audio to wav
#     audio = AudioSegment.from_file(audio_file)
#     # Slice the audio
#     start_time = start_time * 1000  # convert to milliseconds
#     end_time = end_time * 1000  # convert to milliseconds
#     audio = audio[start_time:end_time]
#     # Export as mp3
#     audio.export(audio_file_mp3, format="mp3")
#     # Remove the original mp4 file
#     os.remove(audio_file)
#
#
# # Use the function
# download_audio_clip(
#     "https://www.youtube.com/watch?v=-ugySiRfbZo",
#     3225,
#     3893,
#     "/home/pedro/Desktop/Igreja/RR",
# )
#
