import subprocess

def convert_video_to_audio(video_file, audio_file):
    command = f"ffmpeg -i {video_file} -vn -ab 128k -ar 44100 -y {audio_file}"
    subprocess.call(command, shell=True)
    print(f"Audio file saved as: {audio_file}")

if __name__ == "__main__":
    # Input your file paths here.
    video_file = "video.mp4"
    audio_file = "output.mp3"
    convert_video_to_audio(video_file, audio_file)
