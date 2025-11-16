import os
import requests

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = os.getenv('OPENWEATHER_API_KEY', '4c9de15091549573bf6287df35965b98')
city = 'Nairobi'
params = {
    'q': city,
    'appid': API_KEY,
    'units': 'metric'
}

try:
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Request failed: {e}")
else:
    data = response.json()
    # Safe extraction with error handling in case the API response format changes
    try:
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        city_name = data.get('name', city)
    except (KeyError, IndexError) as e:
        print('Unexpected response format:', e)
    else:
        weather_info = {
            "City": city_name,
            "Temperature (C)": temp,
            "Humidity": humidity,
            "Description": weather_desc,
        }
        print(weather_info)
