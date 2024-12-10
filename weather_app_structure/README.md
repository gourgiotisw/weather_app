
# Weather App

A command-line weather application that fetches current weather and 5-day forecasts for cities using the OpenWeatherMap API.

## Table of Contents
- [Weather App](#weather-app)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Set Up a Virtual Environment (Optional but Recommended)](#2-set-up-a-virtual-environment-optional-but-recommended)
    - [3. Install Dependencies](#3-install-dependencies)
    - [4. Obtain an OpenWeatherMap API Key](#4-obtain-an-openweathermap-api-key)
  - [Configuration](#configuration)
  - [Usage](#usage)
    - [Main Menu Options](#main-menu-options)
  - [Project Structure](#project-structure)
  - [Dependencies](#dependencies)
  - [Contributing](#contributing)
    - [Fork the Repository:](#fork-the-repository)
    - [Clone Your Fork:](#clone-your-fork)
    - [Create a Feature Branch:](#create-a-feature-branch)
    - [Commit Your Changes:](#commit-your-changes)
    - [Push to the Branch:](#push-to-the-branch)
    - [Open a Pull Request:](#open-a-pull-request)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)
  - [Additional Notes](#additional-notes)
  - [Common Issues and Solutions](#common-issues-and-solutions)
    - [Invalid API Key Error](#invalid-api-key-error)
    - [Module Not Found Errors](#module-not-found-errors)
    - [Virtual Environment Issues](#virtual-environment-issues)
  - [Contact and Support](#contact-and-support)

## Features
- **Current Weather Information**: Fetches and displays current weather data in Fahrenheit for any city.
- **5-Day Forecast**: Provides a 5-day weather forecast with average temperatures and conditions.
- **Favorites Management**: Allows you to save favorite cities for quick access and remove them as needed.
- **User-Friendly Interface**: Features input validation and clear prompts to enhance user experience.
- **Error Handling**: Handles invalid inputs, network errors, and API errors gracefully.
- **Colored Output**: Uses `colorama` to add color to terminal output for better readability.

## Prerequisites
- **Python 3.6 or Higher**: Ensure you have Python installed. You can check your Python version by running:
  ```bash
  python --version
  ```
- **OpenWeatherMap API Key**: You need an API key from OpenWeatherMap to access the weather data.

## Installation

### 1. Clone the Repository
Clone the repository to your local machine using Git:
```bash
git clone https://github.com/yourusername/weather_app.git
cd weather_app
```
(Replace `yourusername` with your GitHub username if applicable.)

### 2. Set Up a Virtual Environment (Optional but Recommended)
- On Windows:
  ```bash
  python -m venv venv
  venv\Scriptsctivate
  ```
- On macOS/Linux:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
Install the required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

### 4. Obtain an OpenWeatherMap API Key
1. Register on OpenWeatherMap:
   - Visit [OpenWeatherMap Sign Up](https://home.openweathermap.org/users/sign_up).
   - Create a free account by providing the necessary information.
2. Retrieve Your API Key:
   - After logging in, navigate to the API keys section.
   - Copy your unique API key.

## Configuration
Update the `config.ini` file with your API key:
```ini
[DEFAULT]
API_KEY = your_actual_api_key
```
_Important_: Replace `your_actual_api_key` with the API key you obtained from OpenWeatherMap.

## Usage
Run the application from the project's root directory:
```bash
python main.py
```
Follow the on-screen prompts to interact with the application.

### Main Menu Options
- **Get Weather by City**:
  - Enter a city name to fetch the current weather.
  - Optionally, view the 5-day forecast.
  - Optionally, save the city to your favorites.
- **Show Favorite Cities**:
  - Displays a list of your favorite cities.
  - Select a city to view its current weather and forecast.
- **Remove a City from Favorites**:
  - Remove a city from your favorites list.
- **Exit**: Closes the application.

## Project Structure
```arduino
weather_app/
├── config.ini
├── main.py
├── requirements.txt
└── weather_app/
    ├── __init__.py
    ├── services.py
    └── utils.py
```
- `config.ini`: Configuration file containing your API key.
- `main.py`: Entry point of the application.
- `requirements.txt`: Lists all Python dependencies.
- `weather_app/`: Package directory containing the application's modules.
  - `__init__.py`: Indicates that `weather_app` is a Python package.
  - `services.py`: Contains functions for fetching weather data and managing favorites.
  - `utils.py`: Utility functions for input handling and menu display.

## Dependencies
The application depends on the following Python packages:
- `requests`: For making HTTP requests to the API.
- `colorama`: For colored terminal output.
- `configparser`: For handling configuration files.

These are listed in `requirements.txt` and can be installed using:
```bash
pip install -r requirements.txt
```

## Contributing
Contributions are welcome! If you'd like to contribute:

### Fork the Repository:
Click the "Fork" button at the top of the repository page.

### Clone Your Fork:
```bash
git clone https://github.com/yourusername/weather_app.git
```

### Create a Feature Branch:
```bash
git checkout -b feature/YourFeature
```

### Commit Your Changes:
```bash
git commit -am "Add new feature"
```

### Push to the Branch:
```bash
git push origin feature/YourFeature
```

### Open a Pull Request:
Go to your fork on GitHub and open a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgments
- **OpenWeatherMap API**: Provides the weather data used in this application.
- **Colorama**: Used for colored terminal output.
- **Python Software Foundation**: For the Python programming language.

## Additional Notes
- **Favorites File**: The `favorites.txt` file is created in the project root when you save your first favorite city. It is ignored by Git via `.gitignore`.
- **Error Handling**: The application includes enhanced error handling for network issues and invalid API responses.
- **Python Version**: Ensure you're using Python 3.6 or higher for compatibility.

## Common Issues and Solutions

### Invalid API Key Error
- **Problem**: Receiving an error message about an invalid API key.
- **Solution**:
  - Verify that your API key is correctly entered in the `config.ini` file.
  - Ensure that your OpenWeatherMap account is active and the API key is valid.
  - Wait up to 2 hours after generating a new API key for it to become active.

### Module Not Found Errors
- **Problem**: Import errors such as `ModuleNotFoundError` or `ImportError`.
- **Solution**:
  - Ensure all dependencies are installed using `pip install -r requirements.txt`.
  - Activate your virtual environment if you're using one.
  - Check that you're running `main.py` from the project's root directory.

### Virtual Environment Issues
- **Problem**: Problems activating or using the virtual environment.
- **Solution**:
  - Recreate the virtual environment:
    ```bash
    python -m venv venv
    ```
  - Activate the virtual environment before installing dependencies and running the application.

## Contact and Support
If you have any questions or need further assistance:
- **OpenWeatherMap API Documentation**: [API Docs](https://openweathermap.org/api)
- **Python Documentation**: [Python Docs](https://docs.python.org/3/)
- **GitHub Issues**: Feel free to open an issue on the repository.
