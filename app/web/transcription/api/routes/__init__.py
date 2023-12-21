from flask import Blueprint

transcription_bp = Blueprint('transcription', __name__)

from transcription.api.routes import routes
