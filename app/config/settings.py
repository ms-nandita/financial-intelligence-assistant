from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    OPEN_API_KEY = os.getenv("OPENAPI_KEY")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

settings = Settings()