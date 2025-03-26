import os
from dotenv import load_dotenv

load_dotenv()

# Twilio Credentials
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_FROM = os.getenv(
    "TWILIO_WHATSAPP_FROM"
)  # e.g., 'whatsapp:+14155238886'
WHATSAPP_TO = os.getenv(
    "WHATSAPP_TO"
)  # e.g., 'whatsapp:+your_number'
