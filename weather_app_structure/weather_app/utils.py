import os
import configparser
from colorama import init, Fore

init(autoreset=True)


def get_api_key():
    """Retrieves the API key from environment variable or config file."""
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if api_key:
        return api_key
    config = configparser.ConfigParser()
    config_file_path = os.path.join(os.path.dirname(__file__), '..', 'config.ini')
    if os.path.exists(config_file_path):
        config.read(config_file_path)
        api_key = config['DEFAULT'].get('API_KEY')
        if api_key and api_key != 'your_actual_api_key':
            return api_key
    print(Fore.RED + "Error: OpenWeatherMap API key not found or invalid.")
    print("Please set your API key in the config.ini file or as an environment variable.")
    exit(1)


def get_user_confirmation(prompt):
    """Utility function to get yes/no confirmation from the user."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")


def display_menu():
    """Displays the main menu."""
    print(Fore.CYAN + "\nWeather App")
    print("1. Get weather by city")
    print("2. Show favorite cities")
    print("3. Remove a city from favorites")
    print("4. Exit")
