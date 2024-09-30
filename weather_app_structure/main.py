from weather_app.services import (
    get_weather,
    get_forecast,
    save_favorite,
    load_favorites,
    remove_favorite,
)
from weather_app.utils import display_menu, get_user_confirmation


def main():
    """Main function to run the weather app."""
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            city = input("Enter city name: ").strip()
            if not city:
                print("City name cannot be empty.")
                continue
            if get_weather(city):
                if get_user_confirmation("Do you want to see the forecast? (y/n): "):
                    get_forecast(city)
                if get_user_confirmation("Do you want to save this city to favorites? (y/n): "):
                    save_favorite(city)
        elif choice == '2':
            favorites = load_favorites()
            if not favorites:
                print("No favorite cities saved.")
            else:
                print("\nFavorite Cities:")
                for idx, city in enumerate(favorites, 1):
                    print(f"{idx}. {city.title()}")
                selection = input(
                    "Enter the number of the city to get weather info, or press Enter to go back: "
                ).strip()
                if selection.isdigit():
                    index = int(selection) - 1
                    if 0 <= index < len(favorites):
                        city = favorites[index]
                        if get_weather(city):
                            if get_user_confirmation("Do you want to see the forecast? (y/n): "):
                                get_forecast(city)
                    else:
                        print("Invalid selection.")
                else:
                    continue
        elif choice == '3':
            favorites = load_favorites()
            if not favorites:
                print("No favorite cities to remove.")
            else:
                print("\nFavorite Cities:")
                for idx, city in enumerate(favorites, 1):
                    print(f"{idx}. {city.title()}")
                selection = input(
                    "Enter the number of the city to remove, or press Enter to go back: "
                ).strip()
                if selection.isdigit():
                    index = int(selection) - 1
                    if 0 <= index < len(favorites):
                        city = favorites[index]
                        remove_favorite(city)
                    else:
                        print("Invalid selection.")
                else:
                    continue
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
