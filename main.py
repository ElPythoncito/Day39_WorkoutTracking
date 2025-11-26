# ---------------------------- EL PYTHONCITO XD 🐍🐍🐍🐍!!!!
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os

# ---------------------------------------------------- NUTRITIONIX 🌐
APP_ID = os.getenv("app_id")
API_KEY = os.getenv("api_key")
nutritionix_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
data = {
    "query": input("What activity did you do?🐍: ")
}

response_nutritionix = requests.post(url=nutritionix_endpoint, headers=headers, json=data)
result = response_nutritionix.json()

# ----------------------------------------------- SHEETY 🌐
ENDPOINT_SHEETY = os.getenv("endpoint_sheety")
USER = os.getenv("user")
PASSWORD = os.getenv("password")
TOKEN = os.getenv("token")

headers = {
    "Authorization": TOKEN
}

basic = HTTPBasicAuth(USER, PASSWORD)

day = datetime.today().strftime("%d/%m/%Y")
hour = datetime.today().strftime("%H:%M:%S")
activity = result["exercises"][0]["name"].title()
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]

parameters = {
    "workout": {
        "date": day,
        "time": hour,
        "activity": activity,
        "duration": duration,
        "calories": calories,
    }
}

response_sheety = requests.post(url=ENDPOINT_SHEETY, headers=headers, json=parameters, auth=basic)
print(f"\n\n{response_sheety.status_code}")
