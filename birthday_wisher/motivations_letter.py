# import smtplib
#
#
# my_email = "andysmith2512@gmail.com"
# password = "@Fingerboard2512"
#
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()  # secures connection
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="work@andysmith.is",
#         msg="Subject: Test\n\nTest"
#     )


import datetime as dt
import random
import smtplib

now = dt.datetime.now()

year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
date_of_birth = dt.datetime(year=1987, month=12, day=25)
print(day_of_week)


my_email = "andysmith2512@gmail.com"
password = "@Fingerboard2512"

if day_of_week == 0:
    with open("quotes.txt") as messages:
        quotes = messages.readlines()

        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # secures connection
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="work@andysmith.is",
            msg=f"Subject:Motivational Quote\n\n{quote}"
        )

