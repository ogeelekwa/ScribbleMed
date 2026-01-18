import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "Clinical AI Notetaker"
    DEBUG_MODE: bool = True
    
    # OpenAI Settings
    OPENAI_API_KEY: str

    # Email Settings (SMTP)
    # These default to empty strings so the app doesn't crash if you haven't set them up yet
    SMTP_SERVER: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_FROM_EMAIL: str = "noreply@gmail.com"

    class Config:
        # This tells Pydantic to read from the .env file
        env_file = ".env"

# Create a global instance
settings = Settings()