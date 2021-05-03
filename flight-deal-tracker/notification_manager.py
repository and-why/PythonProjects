from keys import TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID, TWILIO_PHONE_NUMBER, EMAIL_PW, EMAIL
from twilio.rest import Client
import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def send_sms_notification(self, body):
        print(body)
        account_sid = TWILIO_ACCOUNT_SID
        auth_key = TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_key)
        message = client.messages.create(
            body=body,
            to="+61467276127",
            from_=TWILIO_PHONE_NUMBER,
        )
        print(message.sid)

    def create_message(self, data):
        message = ""
        for row in data:
            message += f"{row['currency']} {row['price']}:\n" \
                       f"{row['cityFrom']}({row['fromCode']}) to " \
                       f"{row['cityTo']}({row['toCode']}) - " \
                       f"{row['countryName']}\n" \
                       f"Departs: {row['departureDate']}. Returns: {row['returnDate']}\n" \
                       f"Book here: {row['bookingLink']}'\n" \
                       f"---------------------------------------------------------------------\n\n\n"
        return message

    def send_gmail_email(self, user_email, message):

        print(message)
        with smtplib.SMTP('smtp.gmail.com') as mail_server:
            mail_server.starttls()
            mail_server.login(user=EMAIL, password=EMAIL_PW)
            mail_server.sendmail(
                from_addr=EMAIL,
                to_addrs=user_email,
                msg=f"Subject: Flight deals \n\n\n{message}"
            )
            

