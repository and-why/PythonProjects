import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

today = datetime.today()
TODAY = str(today.strftime('%Y%m%d'))
print(TODAY)

USERNAME = "andysmith"
TOKEN = "jfauh8EOQ_241HGD_dalfnfds3"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create User
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_params = {
    "id": "workouts",
    "name": "Micro workouts",
    "unit": "minutes",
    "type": "int",
    "timezone": "Australia/Melbourne",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/"


# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}"

pixel_creation = {
    "date": TODAY,
    "quantity": "6"
}
#
# response = requests.post(url=pixel_update_endpoint, headers=headers, json=pixel_creation)
# print(response.text)


# updatepixels

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}/{TODAY}"

pixel_updates = {
    "quantity": "3"
}

# response = requests.put(url=update_pixel_endpoint, headers=headers, json=pixel_updates)
# print(response.text)


# delete user

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}/{TODAY}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)