import requests
from twilio.rest import Client

LAT = -23.550520
LON = -46.633308

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "15c4c964cc370aac12ba892311944b9f"

# account_sid = ""
auth_token = "token"

weather_params = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
    "cnt": 4,
    }

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(auth_token)
    message = client.messages.create(
        body="It's going to rain today! Remember to bring an umbrella ☂️",
        from_="+18106786356",
        to="+5511939565734",
    )
    print(message.status)