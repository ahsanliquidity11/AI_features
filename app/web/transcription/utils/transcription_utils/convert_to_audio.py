import subprocess

def convert_meet_recording_to_audio(input_file, output_file):
    try:
        subprocess.run(
            [
                "ffmpeg",
                "-i",
                input_file,
                "-vn",
                "-acodec",
                "libmp3lame",
                "-q:a",
                "2",
                output_file,
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        print("Conversion successful!")
    except subprocess.CalledProcessError as e:
        print("FFmpeg error output:", e.stderr)
        raise