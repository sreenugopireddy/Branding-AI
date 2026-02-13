import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GROQ_KEY = os.getenv("GROQ_API_KEY")
    MODEL = "llama-3.3-70b-versatile"
