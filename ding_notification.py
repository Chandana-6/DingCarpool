import time
from some_notification_library import send_email, send_sms  # Hypothetical library

def send_notification(user_id, message, notification_type="email"):
    if notification_type == "email":
        send_email(user_id, message)
    elif notification_type == "sms":
        send_sms(user_id, message)
    else:
        print("Unknown notification type")

