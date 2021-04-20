import pandas
import datetime as dt
import smtplib
import random

MY_EMAIL = "andysmith2512@gmail.com"
PASSWORD = "#########"

data_file = pandas.read_csv("birthdays.csv")
data_dict = data_file.to_dict(orient="records")

now = dt.datetime.now()
current_day = now.day
current_month = now.month


for person in data_dict:
    if person["day"] == current_day and person["month"] == current_month:
        letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(letter) as letter:
            content = letter.read()
            content = content.replace("[NAME]", person["name"])

            with smtplib.SMTP("smtp.gmail.com") as mail_server:
                mail_server.starttls()
                mail_server.login(user=MY_EMAIL, password=PASSWORD)
                mail_server.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=person["email"],
                    msg=f"Subject:Happy Birthday\n\n{content}"
                )




