from twilio.rest import Client
from config import TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_FROM, WHATSAPP_TO
from utils import get_random_insult

def send_whatsapp_message(body):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.api.account.messages.create(
        from_=TWILIO_WHATSAPP_FROM,
        body=body,
        to=WHATSAPP_TO
    )
    print(f"Sent message: {message.sid}")

if __name__ == "__main__":
    insult = get_random_insult()
    send_whatsapp_message(insult)
