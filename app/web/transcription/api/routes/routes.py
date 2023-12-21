from flask import request
from datetime import datetime
from transcription.api.routes import transcription_bp
from flask import jsonify
from flask import  request, jsonify

import os

from ...utils.transcription_utils.convert_to_audio import convert_meet_recording_to_audio
from ...utils.transcription_utils.divide_segments import divide_segments
from ...utils.transcription_utils.create_pdf import create_pdf
from ...utils.transcription_utils.remove_repitions import remove_repetitions

    
@transcription_bp.route("/")
def hello_world():
    try:
        print("env_api", os.getenv("OPENAI_KEY"))
        return "<p>Hello, World!</p>"
    except Exception as e:
        return jsonify({"error": str(e)})

@transcription_bp.route('/transcribe_audio', methods=['POST'])
def transcribe_audio_endpoint():
    try:
        print("Hello, World! from routes", request)
        data = request.json
        file_path = data.get("file_path")

        now = datetime.now()
        date_time_str = now.strftime("%Y%m%d_%H%M%S")
        output_file = f"output_{date_time_str}.mp3"

        convert_meet_recording_to_audio(file_path, output_file)

        transcripts = divide_segments(output_file, segment_size_mb=24)

        cleaned_transcripts = [remove_repetitions(transcript, sequence_length=1) for transcript in transcripts]

        pdf_filename = create_pdf(cleaned_transcripts)

        os.remove(output_file)

        return jsonify({"transcripts": transcripts, "pdf_filename": pdf_filename})
    except Exception as e:
        return jsonify({"error": str(e)}),500
