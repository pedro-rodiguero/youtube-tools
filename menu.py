import os
from download_video_only import download_video
from download_video_audio import download_video_as_audio
from download_audio import download_audio_clip
from convert_to_mp4 import convert_webm_to_mp4
from double_frames import double_frames


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main_menu():
    while True:
        clear_screen()
        print("YouTube Tools Menu")
        print("===================")
        print("1. Download Video Only")
        print("2. Download Video as Audio")
        print("3. Download Audio Clip")
        print("4. Convert WebM to MP4")
        print("5. Double Video Frames")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            url = input("Enter YouTube URL: ")
            path = input("Enter save path: ")
            download_video(url, path)
        elif choice == "2":
            url = input("Enter YouTube URL: ")
            path = input("Enter save path: ")
            download_video_as_audio(url, path)
        elif choice == "3":
            url = input("Enter YouTube URL: ")
            path = input("Enter save path: ")
            download_audio_clip(url, path)
        elif choice == "4":
            input_path = input("Enter WebM file path: ")
            output_path = input("Enter MP4 save path: ")
            convert_webm_to_mp4(input_path, output_path)
        elif choice == "5":
            input_path = input("Enter video file path: ")
            output_path = input("Enter save path for doubled frames video: ")
            double_frames(input_path, output_path)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main_menu()
