import json
from openai import AsyncOpenAI
from src.config import settings

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are an expert medical scribe. Convert the consultation transcript into a JSON object with these exact fields:
- subjective: Patient's complaints.
- objective: Observations and vitals.
- assessment: Diagnosis and analysis.
- plan: Treatment and follow-up.
- patient_summary: A simple, empathetic summary for the patient (non-medical language).
"""

async def generate_soap_note(transcript: str) -> dict:
    try:
        response = await client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": transcript}
            ],
            response_format={ "type": "json_object" }
        )
        
        content = response.choices[0].message.content
        return json.loads(content)
    except Exception as e:
        print(f"LLM Error: {e}")
        raise e