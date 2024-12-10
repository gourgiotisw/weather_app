import requests
import os
import datetime
from urllib.parse import quote
from .utils import get_api_key
from colorama import Fore

API_KEY = get_api_key()
BASE_URL = 'https://api.openweathermap.org/data/2.5/'


def get_weather(city):
    """Fetches and displays current weather for a given city."""
    city_encoded = quote(city)
    url = f"{BASE_URL}weather?q={city_encoded}&appid={API_KEY}&units=imperial"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print(Fore.RED + "Error: Invalid API key. Please check your API key and try again.")
        else:
            print(Fore.RED + f"HTTP error occurred: {http_err}")
        return False
    except requests.exceptions.RequestException as req_err:
        print(Fore.RED + f"Request error occurred: {req_err}")
        return False
    except Exception as err:
        print(Fore.RED + f"An error occurred: {err}")
        return False

    temp = data['main'].get('temp')
    weather = data['weather'][0].get('description')
    wind_speed = data['wind'].get('speed')
    humidity = data['main'].get('humidity')

    if temp is None or weather is None:
        print(Fore.RED + "Error retrieving weather data.")
        return False

    print(Fore.BLUE + f"\nCurrent temperature in {city.title()}: {temp}°F")
    print(Fore.GREEN + f"Weather conditions: {weather.title()}")
    print(f"Wind Speed: {wind_speed} mph")
    print(f"Humidity: {humidity}%")
    return True


def get_forecast(city):
    """Fetches and displays 5-day forecast for a given city."""
    city_encoded = quote(city)
    url = f"{BASE_URL}forecast?q={city_encoded}&appid={API_KEY}&units=imperial"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print(Fore.RED + "Error: Invalid API key. Please check your API key and try again.")
        else:
            print(Fore.RED + f"HTTP error occurred: {http_err}")
        return
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        return

    forecasts = {}
    for item in data['list']:
        date = datetime.datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S').date()
        temp = item['main'].get('temp')
        weather = item['weather'][0].get('description')
        if date not in forecasts:
            forecasts[date] = {'temps': [], 'weather': []}
        forecasts[date]['temps'].append(temp)
        forecasts[date]['weather'].append(weather)

    print(Fore.CYAN + f"\n5-Day Forecast for {city.title()}:")
    for date, info in forecasts.items():
        avg_temp = sum(info['temps']) / len(info['temps'])
        weather_desc = max(set(info['weather']), key=info['weather'].count)
        print(f"{date}: {avg_temp:.1f}°F, {weather_desc.title()}")


def save_favorite(city):
    """Saves a city to the favorites list."""
    favorites = load_favorites()
    city = city.strip()
    if city.lower() in [fav.lower() for fav in favorites]:
        print(f"{city.title()} is already in your favorites.")
    else:
        with open('favorites.txt', 'a') as f:
            f.write(f"{city}\n")
        print(f"{city.title()} has been added to your favorites.")


def load_favorites():
    """Loads favorite cities from the local file."""
    if not os.path.exists('favorites.txt'):
        return []
    with open('favorites.txt', 'r') as f:
        favorites = [line.strip() for line in f if line.strip()]
    return favorites


def remove_favorite(city):
    """Removes a city from the favorites list."""
    favorites = load_favorites()
    city = city.strip()
    if city.lower() in [fav.lower() for fav in favorites]:
        favorites = [fav for fav in favorites if fav.lower() != city.lower()]
        with open('favorites.txt', 'w') as f:
            for fav in favorites:
                f.write(f"{fav}\n")
        print(f"{city.title()} has been removed from your favorites.")
    else:
        print(f"{city.title()} is not in your favorites.")
