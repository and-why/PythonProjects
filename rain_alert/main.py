import os
import requests

import api_keys
from api_keys import open_weather_api_key, twilio_keys
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https': os.environ['https_proxy']}

params = {
    "lat": -38.171021,
    "lon": 144.717453,
    "appid": open_weather_api_key,
    # "appid": os.environ.get("OWM_API_KEY"),
    "units": "metric",
    "exclude": "current,minutely,daily"
}

# account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
# auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
account_sid = twilio_keys["account_sid"]
auth_token = twilio_keys["auth_token"]

# Quibdo
params_rain = {
    "lat": 5.6956,
    "lon": 76.6498,
    "appid": open_weather_api_key,
    "units": "metric",
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=params_rain)
response.raise_for_status()
weather_data = response.json()["hourly"]

weather_data = weather_data[:12]

will_rain = False

for hour in weather_data:
    weather_id = hour["weather"][0]["id"]
    if weather_id < 900:
        will_rain = True


# , "+61413088617"
phone_to = ["+61467276127"]

for phone_number in phone_to:
    if will_rain:
        print("will rain")
        client = Client(account_sid, auth_token)
        message = client.messages.create(body="It's going to rain today, don't put washing outside.",
                                         from_=twilio_keys["phone_number"],
                                         to=phone_number)
        print(message.status)

