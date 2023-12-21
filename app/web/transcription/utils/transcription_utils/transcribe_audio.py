import os
import openai


def transcribe_audio(file_path):
    file_size = os.path.getsize(file_path)
    file_size_in_mb = file_size / (1024 * 1024)
    if file_size_in_mb < 25:
        with open(file_path, "rb") as audio_file:
            response = openai.Audio.transcribe(
                model="whisper-1",
                file=audio_file,
                language='en'
            )
            transcription_text = response.text
        return transcription_text
    else:
        print("Please provide a smaller audio file (max 25mb).")