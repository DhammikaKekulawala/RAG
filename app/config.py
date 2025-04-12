import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API Key configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Define directories
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
DOCUMENTS_DIR = os.path.join(DATA_DIR, "documents")
CHROMA_DIR = os.path.join(DATA_DIR, "chroma_db")

# Create directories if they do not exist
os.makedirs(DOCUMENTS_DIR, exist_ok=True)
os.makedirs(CHROMA_DIR, exist_ok=True)
