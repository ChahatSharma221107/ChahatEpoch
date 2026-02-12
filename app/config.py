import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MODEL_NAME = "gpt-4o-mini"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    TEMPERATURE = 0.2
    MAX_TOKENS = 2000
