
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()



class Config(object):
    OPENAI_KEY = os.getenv("OPENAI_API_KEY")  # Access environment variable directly
    PINECONE_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_ENV = os.getenv("PINECONE_API_ENV")
    index_name = os.getenv("index_name")



class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False
