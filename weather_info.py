import os

import requests
from dotenv import load_dotenv

load_dotenv()

def getIP():
    response = requests.get("https://api64.ipify.org?format=json")
    data = response.json()
    return data['ip']

def getCity():
    ip_address = getIP()
    api_key = os.getenv("city_api_key")
    response = requests.get(f"https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}&ip_address={getIP()}")
    data = response.json()
    return data["city"]
    # return 'Philadelphia'  // Backup in case api limit is reached

def getWeather(city=getCity()):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    api_key = os.getenv("weather_api_key")
    full_url = url + "q=" + city + "&appid=" + api_key + "&units=imperial"

    response = requests.get(full_url)

    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        temperature = main["temp"]
        humidity = main["humidity"]
        pressure = main["pressure"]
        report = data["weather"]

        weather_data = {
            "city" : city,
            "temperature": int(temperature),
            "humidity": humidity,
            "pressure": pressure,
            "report": report[0]['description']
        }
        return weather_data
        #print(f"{city:-^30}")
        #print(f"Temperature: {int(temperature)}"+chr(176)+"F")
        #speak(f"Temperature in{city} is {int(temperature)} degrees Fahrenheit.")
        #print(f"Humidity: {humidity}%")
        #speak(f"Humidity is {humidity}%")
        #print(f"Pressure: {pressure}")
        #speak(f"Pressure is {pressure}")
        #print(f"Weather Report: {report[0]['description']}")
        #speak(f"Weather report is {report[0]['description']}")

    else:
        print("Error in the HTTP request: ", str(response.status_code))
        return -1
