from keys import API_KEY, APP_ID, BEARER
import requests
from _datetime import datetime


GENDER = "male"
WEIGHT_KG = 71
HEIGHT_CM = 173
AGE = 33

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}
sheet_headers = {
    "Authorization": BEARER
}

user_input = input("Tell me what you did: \n")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=params, headers=headers)
response.raise_for_status()
response = response.json()
print(response["exercises"][0]["name"])

for exercise in response["exercises"]:
    exercise_post = {
        "workout": {
            "date": datetime.today().strftime("%d/%m/%Y"),
            "time": datetime.today().strftime("%H:%M:%S"),
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"], }
    }

    print(exercise_post)

    sheet_endpoint = "https://api.sheety.co/518dfb4222e8b9c20571d23cefbed8c9/myWorkouts/workouts"

    post_exercise = requests.post(url=sheet_endpoint, headers=sheet_headers, json=exercise_post)
    print(post_exercise.text)