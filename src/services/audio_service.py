#Handles Whisper transcription.
import os
from fastapi import UploadFile
from openai import AsyncOpenAI
from src.config import settings

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

async def transcribe_audio(file: UploadFile) -> str:
    temp_filename = f"temp_{file.filename}"
    
    try:
        # Save temp file
        with open(temp_filename, "wb") as buffer:
            buffer.write(await file.read())

        # Transcribe
        with open(temp_filename, "rb") as audio_file:
            transcript = await client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file
            )
        
        return transcript.text

    except Exception as e:
        print(f"Transcription failed: {e}")
        raise e
        
    finally:
        # cleanup
        if os.path.exists(temp_filename):
            os.remove(temp_filename)