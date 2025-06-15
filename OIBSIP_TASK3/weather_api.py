# weather_api.py

import requests
from config import API_KEY, CURRENT_WEATHER_URL, FORECAST_URL

def fetch_current_weather(city, units='metric'):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': units
    }
    try:
        response = requests.get(CURRENT_WEATHER_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

def fetch_forecast(city, units='metric'):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': units
    }
    try:
        response = requests.get(FORECAST_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
