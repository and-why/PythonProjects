from datetime import datetime, timedelta
from keys import TEQUILA_SEARCH_API_KEY, TEQUILA_ENDPOINT
import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.headers = {
            "apikey": TEQUILA_SEARCH_API_KEY,
            "accept": "application/json"
        }
    def get_flight_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=location_endpoint, headers=self.headers, params=params)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def get_flight_country_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=location_endpoint, headers=self.headers, params=params)
        results = response.json()["locations"]
        code = results[0]['country']['id']
        return code

    def get_flight_city_name(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=location_endpoint, headers=self.headers, params=params)
        results = response.json()["locations"]
        # print(results)
        cityName = results[0]['id']
        return cityName

    def get_top_destinations(self, term, country_code):
        top_destination_endpoint = f"{TEQUILA_ENDPOINT}/locations/topdestinations"
        params = {
            "term": term,
            "limit": 100,
        }
        response = requests.get(url=top_destination_endpoint, headers=self.headers, params=params)
        results = response.json()['locations']
        # print(results)
        top_destinations = [result['code'] for result in results if result['country']['code'] != country_code]
        return top_destinations
