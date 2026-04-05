import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
messaging_service_sid = os.getenv("TWILIO_PHONE_NUMBER")

client = Client(account_sid, auth_token)


def send_sms(phone, message):
    message = client.messages.create(
        messaging_service_sid=messaging_service_sid,
        body=message,
        to=phone
    )