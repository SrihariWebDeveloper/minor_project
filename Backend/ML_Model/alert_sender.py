from db import users_collection
from sms_service import send_sms
from alert_message import create_alert_message


def notify_users(alert):

    users = users_collection.find()

    message = create_alert_message(alert)
    
    for user in users:

        phone = user["mobile"]

        try:
            send_sms(phone, message)
        except Exception as e:
            print("SMS failed:", e)