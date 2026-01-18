from pydantic import BaseModel
from typing import Optional

# 1. Note Structure that will be generated
class SoapNoteSchema(BaseModel):
    subjective: str
    objective: str
    assessment: str
    plan: str
    patient_summary: str

# 2. Standard API Response (To be sent back to the frontend)
class ConsultationResponse(BaseModel):
    status: str
    message: str
    data: Optional[SoapNoteSchema] = None

# 3. Schema for Email Request (Internal use)
class EmailPayload(BaseModel):
    recipient_email: str
    subject: str
    body: str
    attachment_path: Optional[str] = None