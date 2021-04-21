import requests

params = {
    "amount": 10,
    "type": "boolean",
    # "difficulty": "medium",
    # "category": 9
}

with requests.get("https://opentdb.com/api.php?", params=params) as question_data:
    question_data.raise_for_status()
    question_data = question_data.json()["results"]

