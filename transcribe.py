import openai
from pydub import AudioSegment

# Load the audio file
print("Loading audio file...")
song = AudioSegment.from_mp3("output.mp3")

# Define the length of each segment in milliseconds (10 minutes in this case)
segment_length_ms = 10 * 60 * 1000

# Calculate the number of segments needed
num_segments = len(song) // segment_length_ms
print(f"Audio file loaded. It will be split into {num_segments + 1} segments.")

# Initialize an empty string to store the full transcription
full_transcript = ""

# Loop over the audio file, segment by segment
for i in range(num_segments + 1):
    print(f"Processing segment {i + 1} of {num_segments + 1}...")

    # Extract the segment
    segment_start = i * segment_length_ms
    segment_end = (i + 1) * segment_length_ms
    segment = song[segment_start:segment_end]

    # Export the segment to a temporary file
    segment.export("temp.mp3", format="mp3")

    # Open the temporary file
    audio_file = open("temp.mp3", "rb")

    # Transcribe the segment
    print("Transcribing segment...")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print("Transcription complete.")

    # Append the transcript to the full transcription
    full_transcript += transcript.text + "\n"

# Write the full transcription to a file
print("Writing full transcription to file...")
with open("transcript.txt", "w") as file:
    file.write(full_transcript)
print("Transcription written to file 'transcript.txt'.")

print("All done!")
