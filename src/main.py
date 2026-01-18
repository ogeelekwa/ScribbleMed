import os
from fastapi import FastAPI, UploadFile, File, Form, BackgroundTasks, HTTPException
from src.services.audio_service import transcribe_audio
from src.services.llm_service import generate_soap_note
from src.services.pdf_service import create_pdf
from src.services.email_service import send_email
from src.models import ConsultationResponse

app = FastAPI(title="Clinical AI Notetaker")

@app.post("/consultation/process", response_model=ConsultationResponse)
async def process_consultation(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    patient_email: str = Form(...),
    doctor_email: str = Form(...)
):
    try:
        # 1. Transcribe
        transcript = await transcribe_audio(file)

        # 2. Analyze (LLM)
        soap_data = await generate_soap_note(transcript)

        # 3. Create PDF
        pdf_filename = f"consultation_{patient_email.split('@')[0]}.pdf"
        pdf_path = create_pdf(soap_data, filename=pdf_filename)

        # 4. Email (Background Task)
        email_body = f"""
        Dear Patient,
        
        Please find attached the summary of your consultation.
        
        Summary:
        {soap_data['patient_summary']}
        
        Regards,
        ScribbleMed Team
        """
        
        background_tasks.add_task(
            send_email,
            recipients=[patient_email, doctor_email],
            subject="Consultation Summary",
            body=email_body,
            attachment_path=pdf_path
        )

        return ConsultationResponse(
            status="success",
            message="Processing complete. Email queued.",
            data=soap_data
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))