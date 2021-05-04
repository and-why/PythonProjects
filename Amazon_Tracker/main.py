import os

from bs4 import BeautifulSoup
import requests
from math import floor
import smtplib


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,en-AU;q=0.8,en-GB;q=0.7"
}

EMAIL = os.environ.get('EMAIL_ADDRESS')
PASSWORD = os.environ.get('EMAIL_PASSWORD')

items_to_track = [{
    "link": "https://www.amazon.com.au/Instant-Pot-Electric-Multi-Use-Stainless/dp/B07Y1XNXMB/ref=asc_df_B07Y1X61QK"
            "/?tag=googleshopdsk-22&linkCode=df0&hvadid=341793029939&hvpos=&hvnetw=g&hvrand=1777025523737046387"
            "&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9071210&hvtargid=pla-1042045950432&th=1",
    "my_price": 140
}, {
    "link": "https://www.amazon.com.au/Acer-EI491CRP-FreeSync2-UltraWide-Monitor/dp/B07WJVLBTS/ref=sr_1_2?crid"
            "=1BMQ2NMAGHDDX&dchild=1&keywords=49+inch+ultrawide+monitor&qid=1620075628&sprefix=49+inch+%2Caps%2C335"
            "&sr=8-2", "my_price": 1900
}
]


for item in items_to_track:
    website = requests.get(item['link'], headers=headers)
    soup = BeautifulSoup(website.content, 'html.parser')
    actual_price = floor(float(soup.find(id="priceblock_ourprice").getText().strip("$").replace(',', '')))
    product_title = soup.find(id="productTitle").getText().strip()
    item["actual_price"] = actual_price
    item["product_title"] = product_title

print(items_to_track)

for item in items_to_track:
    if item["actual_price"] < item["my_price"]:
        message = f"Subject:Time to buy {item['product_title']}\n\n\nThe item {item['product_title']} is currently " \
                  f"selling for {item['actual_price']}, and you set a price of {item['my_price']}. \n\n" \
                  f"You can buy at this link: {item['link']}"
        with smtplib.SMTP('smtp.google.com') as mail_server:
            mail_server.starttls()
            mail_server.login(user=EMAIL, password=PASSWORD)
            mail_server.sendmail(
                from_addr=EMAIL,
                to_addrs="work@andysmith.is",
                msg=message
            )
