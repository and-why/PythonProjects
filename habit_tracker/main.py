import requests

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "andysmithis"
TOKEN = "jfauh8EOQ£$HGD*dalfnfds3"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create User
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

requests.