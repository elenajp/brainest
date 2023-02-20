# """ The goal of this project is to create a weather app that shows the current weather conditions and forecast for a specific location.

# Here are the steps you can take to create this project:

#     Use the requests library to make an API call to a weather service (e.g. OpenWeatherMap) to retrieve the weather data for a specific location.

#     Use the json library to parse the JSON data returned by the API call.

#     Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons and text boxes.

#     Use the Pillow library to display the weather icons.

#     Use the datetime library to display the current time and date. """

import json
import os
import pprint

import config
import requests

# import tkinter
# import pillow

api_key = config.API_KEY
chosen_city = str(input("Enter city: "))


def select_city(city_name: str):
    """Takes a city name as a user input and returns that city name."""
    try:
        city_name.isalpha()
    except ValueError:
        print("Please enter a valid city.")
        return None
    return city_name


def get_geolocation():
    """Performs a get request on the open weather map api to return the latitude and longitude for a city."""
    city = select_city(chosen_city)
    response = requests.get(
        f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    )
    result = response.json()
    # pprint.pprint(result)
    # print()
    lat = result[0]["lat"]
    lon = result[0]["lat"]
    # print(f"the lat is {lat} and the long is {lon}")
    return lat, lon


def get_current_weather():
    """Takes the latitude and longitude as an input and returns the current weather for the chosen city."""
    lat, lon = get_geolocation()
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    )

    result = response.json()
    # weather = result["weather"]
    temp = result["main"]["temp"]
    feels_like = result["main"]["feels_like"]
    description = result["weather"][0]["description"]
    icon = result["weather"][0]["icon"]

    return temp, feels_like, description, icon


select_city(chosen_city)
get_current_weather()
get_geolocation()
