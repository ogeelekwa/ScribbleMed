# ScribbleMed 

ScribbleMed is an automated medical scribe that streamlines patient consultations. This tool captures audio, transcribes it, structures it into SOAP notes using LLMs, and securely emails a summary PDF to the patient and doctor.

## Features

* **Audio Capture:** Secure ingestion of consultation audio.
* **Speech-to-Text:** High-accuracy transcription using OpenAI Whisper.
* **AI Analysis:** Automated SOAP note generation (Subjective, Objective, Assessment, Plan) via GPT-4.
* **PDF Generation:** Auto-formatted medical reports.
* **Automated Delivery:** Email integration via AWS SES/SMTP.

## Tech Stack

* **Backend:** Python 3.10+, FastAPI
* **AI/ML:** OpenAI Whisper, GPT-4o
* **PDF Engine:** WeasyPrint / ReportLab
* **Infrastructure:** Docker (Optional)

## Installation

1.  **Clone the repo**
    ```bash
    git clone [https://github.com/yourusername/ScribbleMed.git](https://github.com/yourusername/ScribbleMed.git)
    cd ScribbleMed
    ```

2.  **Set up Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Variables**
    Rename `.env.example` to `.env` and populate keys:
    ```ini
    OPENAI_API_KEY=sk-...
    SMTP_SERVER=smtp.gmail.com
    SMTP_PORT=587
    SMTP_USER=your_email@example.com
    SMTP_PASSWORD=your_password
    ```

## ⚡ Usage

Start the server:
```bash
uvicorn src.main:app --reload
