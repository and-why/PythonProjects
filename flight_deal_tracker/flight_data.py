import requests
from keys import TEQUILA_SEARCH_API_KEY, TEQUILA_ENDPOINT
from datetime import datetime, timedelta

headers = {
    "apikey": TEQUILA_SEARCH_API_KEY,
}


class FlightData:
    def __init__(self):
        self.date_from = datetime.today() + timedelta(1)
        self.date_to = datetime.today() + timedelta(180)
        self.date_from = self.date_from.strftime('%d/%m/%Y')
        self.date_to = self.date_to.strftime('%d/%m/%Y')

    def get_flight_prices(self, iata_code, price, origin_city):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        params = {
            "fly_from": origin_city,
            "fly_to": iata_code,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "flighttype": "round",
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 14,
            "one_for_city": 1,
            "max_stopovers": 2,
            "curr": "AUD",
            "price_to": price
        }
        response = requests.get(url=search_endpoint, params=params, headers=headers)
        try:
            results = response.json()["data"][0]
        except IndexError:
            print(f"No flights for {params['fly_from']} to {params['fly_to']}")
            return None
        else:
            cheap_flight_data = {
                "origin": results['cityFrom'],
                "destination": results['cityTo'],
                "price": results["price"],
                "nights": results["nightsInDest"],
                "dateFrom": results["route"][0]["local_departure"].split("T")[0],
                "dateTo": results["route"][1]["local_departure"].split("T")[0]
            }
            return cheap_flight_data

    def get_top_flight_prices(self, iata_code, currency):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        top_flights = []
        params = {
            "fly_from": iata_code,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 14,
            "flight_type": "return",
            "one_for_city": 1,
            "max_stopovers": 2,
            "curr": currency,
            "limit": 10
        }
        response = requests.get(url=search_endpoint, params=params, headers=headers)
        for flight in response.json()["data"]:
            # print(flight)

            flight_data = {
                "cityFrom": flight['cityFrom'].encode('utf-8'),
                "fromCode": flight['flyFrom'],
                "countryFrom": flight['countryFrom']['code'],
                "cityTo": flight['cityTo'].encode('utf-8'),
                "toCode": flight['flyTo'],
                "countryTo": flight['countryTo']['code'],
                "countryName": flight['countryTo']['name'].encode('utf-8'),
                "price": flight['price'],
                "currency": currency,
                "departureDate": flight['route'][0]['local_departure'].split("T")[0],
                "returnDate": flight['route'][1]['local_departure'].split("T")[0],
                "bookingLink": flight['deep_link']
            }
            top_flights.append(flight_data)

        return top_flights

    def get_top_overseas_flight_prices(self, iata_code, currency, top_destinations):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        top_overseas_flights = []
        for destination in top_destinations:
            params = {
                "fly_from": iata_code,
                "fly_to": destination,
                "date_from": self.date_from,
                "date_to": self.date_to,
                "nights_in_dst_from": 3,
                "nights_in_dst_to": 14,
                "flight_type": "return",
                "one_for_city": 1,
                "max_stopovers": 2,
                "curr": currency,
                "limit": 10
            }
            response = requests.get(url=search_endpoint, params=params, headers=headers)
            for flight in response.json()["data"]:
                flight_data = {
                    "cityFrom": flight['cityFrom'].encode('utf-8'),
                    "fromCode": flight['flyFrom'],
                    "countryFrom": flight['countryFrom']['code'],
                    "cityTo": flight['cityTo'].encode('utf-8'),
                    "toCode": flight['flyTo'],
                    "countryTo": flight['countryTo']['code'],
                    "countryName": flight['countryTo']['name'].encode('utf-8'),
                    "price": flight['price'],
                    "currency": currency,
                    "departureDate": flight['route'][0]['local_departure'].split("T")[0],
                    "returnDate": flight['route'][1]['local_departure'].split("T")[0],
                    "bookingLink": flight['deep_link']
                }
                top_overseas_flights.append(flight_data)

        sorted_overseas_flights = sorted(top_overseas_flights, key=lambda k: k['price'])
        return sorted_overseas_flights
