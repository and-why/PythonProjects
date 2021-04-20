import requests
from datetime import datetime
import smtplib
import sched, time
from pw import password, email

MY_LAT = -38.171020
# MY_LAT = 15.171020
MY_LONG = 44.717460
smtp_server = "smtp.gmail.com"
MY_EMAIL = email
PW = password

s = sched.scheduler(time.time, time.sleep)


# Your position is within +5 or -5 degrees of the ISS position.
def check_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if sunrise > time_now > sunset:
        return True


def check_all_true():
    if is_night() and check_position():
        with smtplib.SMTP(smtp_server) as server:
            server.starttls()
            server.login(MY_EMAIL, PW)
            server.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Look up\n\nThe International Space "
                                                                       "Station is somewhere above you. Look up now!")
    s.enter(60, 1, check_all_true)


s.enter(1, 1, check_all_true)
s.run()
