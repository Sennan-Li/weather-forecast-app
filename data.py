import requests

API_Key = "32ae047cbc1c4f25f7c13b1395207710"

def get_data(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_Key}"
    response = requests.get(url)
    data = response.json()
    values = 8 * forecast_days
    weather_data = data["list"][:values]
    return weather_data