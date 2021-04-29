import requests
from keys import SHEET_API_KEY

sheets_endpoint = "https://api.sheety.co/518dfb4222e8b9c20571d23cefbed8c9/flights"

headers = {
    "Authorization": SHEET_API_KEY
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.user_data = {}
        self.flight_endpoint = f"{sheets_endpoint}/flightList"
        self.user_endpoint = f"{sheets_endpoint}/users"

    def get_codes(self):
        response = requests.get(url=self.flight_endpoint, headers=headers).json()
        self.destination_data = response["flightList"]
        return self.destination_data

    def update_sheet(self, sheet):
        if sheet == "user":
            for row in self.user_data:
                new_data = {
                    "user": {
                        "iataCode": row["iataCode"],
                        "country": row['country'],
                        "cityName": row['cityName']
                    }
                }
                response = requests.put(url=f"{self.user_endpoint}/{row['id']}", json=new_data, headers=headers)
                print(response.text)
        else:
            for row in self.destination_data:
                new_data = {
                    "flightlist": {
                        "iataCode": row["iataCode"],
                    }
                }
                response = requests.put(url=f"{self.flight_endpoint}/{row['id']}", json=new_data, headers=headers)
                print(response.text)

    def get_users(self):
        response = requests.get(url=self.user_endpoint, headers=headers).json()
        self.user_data = response['users']
        return self.user_data
