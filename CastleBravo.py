from resource import struct_rusage
from smtpd import usage

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

def weather():
    weatherForecast = ["Snowy", "Blizzard", "Rainy", "Windy", "Icy", "Sunny"]
    weatherCondition = random.choice(weatherForecast)
    return weatherForecast

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "Snowy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 55mph.")
    elif weatherAlert == "Blizzard":
        print("\nThe National Weather Service has updated our alarm by 45 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 45mph.")

vehicleResponseSystem()