import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from typing import List
from src.config import settings

def send_email(recipients: List[str], subject: str, body: str, attachment_path: str = None):
    """
    Sends an email with a PDF attachment via SMTP.
    """
    try:
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = settings.SMTP_FROM_EMAIL
        msg['To'] = ", ".join(recipients)

        # Attach body text
        msg.attach(MIMEText(body, 'plain'))

        # Attach PDF if it exists
        if attachment_path:
            with open(attachment_path, "rb") as f:
                part = MIMEApplication(f.read(), Name=os.path.basename(attachment_path))
                part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
                msg.attach(part)

        # Connect to SMTP Server
        with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            server.send_message(msg)
            
        print(f"Email sent successfully to {recipients}")

    except Exception as e:
        print(f"Failed to send email: {e}")
        # In production, you might want to log this to a file or monitoring service