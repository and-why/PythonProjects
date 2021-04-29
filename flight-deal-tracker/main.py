from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_data = FlightData()
flight_search = FlightSearch()

sheet_data = data_manager.get_codes()
user_data = data_manager.get_users()
notification_manager = NotificationManager()

ORIGIN_CITY = "MEL"

if sheet_data[len(sheet_data) - 1]["iataCode"] == '':
    for row in sheet_data:
        row['iataCode'] = flight_search.get_flight_code(row['destination'])
    data_manager.destination_data = sheet_data
    data_manager.update_sheet("flightList")

if user_data[len(user_data) - 1]["iataCode"] == '':
    for row in user_data:
        row['iataCode'] = flight_search.get_flight_code(row['airport'])
        row['country'] = flight_search.get_flight_country_code(row['airport'])
        row['cityName'] = flight_search.get_flight_city_name(row['airport'])

    data_manager.user_data = user_data
    data_manager.update_sheet("user")

# GET DEALS BASED ON SHEET
# for row in sheet_data:
#     print(f"Checking if {ORIGIN_CITY} to {row['destination']} has any flights cheaper than ${row['lowCost']}...")
#     data = flight_data.get_flight_prices(row["iataCode"], row["lowCost"], ORIGIN_CITY)
#     try:
#         message = f"Price Alert! Only ${data['price']} to fly from {data['origin']} to {data['destination']} for " \
#               f"{data['nights']} nights! Leave on {data['dateFrom']} returning {data['dateTo']}"
#     except TypeError:
#         pass
#     else:
#         notification_manager.send_sms_notification(message)

# cheapest 10 flights:
for row in user_data:
    top_destinations = flight_search.get_top_destinations(row["cityName"], row['country'])
    cheap_flights = flight_data.get_top_flight_prices(row["iataCode"], row['currency'])
    overseas_flights = flight_data.get_top_overseas_flight_prices(row['iataCode'], row['currency'],
                                                                  top_destinations)[:5]

    message = notification_manager.create_message(cheap_flights)
    message += notification_manager.create_message(overseas_flights)

    notification_manager.send_gmail_email(row['email'], message)

