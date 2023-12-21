import os
from .transcribe_audio import transcribe_audio
import math

def divide_segments(file_path, segment_size_mb):
    file_size = os.path.getsize(file_path)
    num_segments = math.ceil(file_size / (segment_size_mb * 1024 * 1024))

    transcripts = []

    with open(file_path, "rb") as audio_file:
        for i in range(num_segments):
            segment_start = i * segment_size_mb * 1024 * 1024
            segment_end = min((i + 1) * segment_size_mb * 1024 * 1024, file_size)
            segment_data = audio_file.read(segment_end - segment_start)

            segment_filename = f"segment_{i}.wav"
            with open(segment_filename, "wb") as segment_file:
                segment_file.write(segment_data)

            transcript = transcribe_audio(segment_filename)
            transcripts.append(transcript)

            os.remove(segment_filename)
            
                
    if file_size > segment_end:
        remaining_data = audio_file.read()
        remaining_filename = "remaining_segment.wav"
        with open(remaining_filename, "wb") as remaining_file:
            remaining_file.write(remaining_data)

        transcript = transcribe_audio(remaining_filename)
        transcripts.append(transcript)

        os.remove(remaining_filename)

    return transcripts