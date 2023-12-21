from flask import Flask
from transcription.api.routes import transcription_bp

def create_app(config_object):
    app = Flask(__name__)
    
    app.config.from_object(config_object)
    
    app.register_blueprint(transcription_bp)

    return app

if __name__ == '__main__':
  
    app = create_app('transcription.config.DevConfig')
    app.run()
