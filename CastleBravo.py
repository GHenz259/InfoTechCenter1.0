

# This line prints the title of the program.
print("Weather Branch\n")

# Import necessary libraries: random for selecting weather conditions, sleep for adding delays in the program.
import random
from time import sleep


# This function randomly selects a weather condition from the list of possible forecasts.
def weather():
    # A list of possible weather conditions.
    weatherForecast = ["Snowy", "Blizzard", "Rainy", "Windy", "Icy", "Sunny"]

    # Randomly selects one weather condition from the list.
    weatherCondition = random.choice(weatherForecast)

    # Returns the selected weather condition.
    return weatherCondition


# Call the weather function and store the result in weatherAlert to use in the VRS system.
weatherAlert = weather()


# This function simulates a Vehicle Response System (VRS) that reacts to weather conditions.
def vehicleResponseSystem():
    # If the weather is Snowy, adjust the alarm and driving speed.
    if weatherAlert == "Snowy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)  # Adds a delay of 1 second.
        print("\nVRS System has been engaged only allowing you to drive 55mph.")

    # If the weather is Blizzard, adjust the alarm and driving speed.
    elif weatherAlert == "Blizzard":
        print("\nThe National Weather Service has updated our alarm by 45 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 45mph.")

    # If the weather is Rainy, adjust the alarm and driving speed.
    elif weatherAlert == "Rainy":
        print("\nThe National Weather Service has updated our alarm by 15 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 65mph.")

    # If the weather is Windy, adjust the alarm and driving speed.
    elif weatherAlert == "Windy":
        print("\nThe National Weather Service has updated our alarm by 15 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 70mph.")

    # If the weather is Icy, adjust the alarm and driving speed.
    elif weatherAlert == "Icy":
        print("\nThe National Weather Service has updated our alarm by 50 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS System has been engaged only allowing you to drive 30mph.")

    # If the weather is Sunny or any other condition, the system allows normal driving.
    else:
        print("The National Weather Service is calling for", weatherAlert,
              "skies, drive carefully to get to your destination!")
        sleep(1)
        print("\nVRS System has been disengaged")

vehicleResponseSystem()