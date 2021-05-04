# IMPORTS
from keys import alpha_vantage, newsapi, twilio_keys
import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCKS = [
    {"SYMBOL": "TSLA",
     "COMPANY_NAME": "Tesla Inc"},
    {"SYMBOL": "IBM",
     "COMPANY_NAME": "IBM"},
]

COMPANY_NAME = "Tesla Inc"
today = datetime.today() - timedelta(3)
today = today.strftime('%Y-%m-%d')
# twilio part
account_sid = twilio_keys["ACCOUNT_SID"]
auth_token = twilio_keys["AUTH_TOKEN"]
client = Client(account_sid, auth_token)

for stock in STOCKS:
    stocks_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock["SYMBOL"],
        "outputsize": "compact",
        "datatype": "json",
        "apikey": alpha_vantage
    }

    data = requests.get("https://www.alphavantage.co/query", params=stocks_params)
    data.raise_for_status()
    data = data.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]

    yesterday_price = float(data_list[1]["4. close"])
    today_price = float(data_list[0]["4. close"])

    percentage_change = round(((today_price - yesterday_price) / yesterday_price) * 100, 2)

    news_params = {
        "q": stock["COMPANY_NAME"],
        "from": today,
        "sortBy": "publishedAt",
        'pageSize': 3,
        "language": "en",
        "apikey": newsapi
    }

    news = requests.get("https://newsapi.org/v2/everything", params=news_params)
    news.raise_for_status()
    news = news.json()

    if percentage_change > 0.5:
        for i in range(0, 3):
            message_body = f"{stock['SYMBOL']} 🔺{percentage_change}%\n" \
                           f"{i + 1}. Headline: {news['articles'][i]['title']}\n" \
                           f"Brief: {news['articles'][i]['description']}\n" \
                           f"Source: {news['articles'][i]['source']['name']}"
            # message = client.messages.create(body=message_body, from_=twilio_keys["FROM_"], to="+61467276127")
            print(message_body)
    elif percentage_change < -0.5:
        for i in range(0, 3):
            message_body = f"{stock['SYMBOL']} 🔻{percentage_change}%\n" \
                           f"{i + 1}. Headline: {news['articles'][i]['title']}\n" \
                           f"Brief: {news['articles'][i]['description']}\n" \
                           f"Source: {news['articles'][i]['source']['name']}"
            # message = client.messages.create(body=message_body, from_=twilio_keys["FROM_"], to="+61467276127")
            print(message_body)
    else:
        pass
