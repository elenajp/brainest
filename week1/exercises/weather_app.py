# """ The goal of this project is to create a weather app that shows the current weather conditions and forecast for a specific location.

# Here are the steps you can take to create this project:

#     Use the requests library to make an API call to a weather service (e.g. OpenWeatherMap) to retrieve the weather data for a specific location.

#     Use the json library to parse the JSON data returned by the API call.

#     Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons and text boxes.

#     Use the Pillow library to display the weather icons.

#     Use the datetime library to display the current time and date. """

import requests
import json
import pprint
import os
import config

# import tkinter
# import pillow

api_key = config.API_KEY
city_name = "New York"


def get_geolocation():
    response = requests.get(
        f"https://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}"
    )
    result = response.json()
    # pprint.pprint(result)
    # print()
    lat = result[0]["lat"]
    lon = result[0]["lat"]
    # print(f"the lat is {lat} and the long is {lon}")
    return lat, lon


def get_current_weather():
    lat, lon = get_geolocation()
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    )

    result = response.json()
    pprint.pprint(result)


get_current_weather()
get_geolocation()
