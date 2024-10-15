

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
    return random.choice(weatherForecast)


# Call the weather function and store the result in weatherAlert to use in the VRS system.
weatherAlert = weather()

# Dictionary for alarm adjustments and speeds based on weather conditions.
weather_responses = {
    "Snowy": {"alarm": 30, "speed": 55},
    "Blizzard": {"alarm": 45, "speed": 45},
    "Rainy": {"alarm": 15, "speed": 65},
    "Windy": {"alarm": 15, "speed": 70},
    "Icy": {"alarm": 50, "speed": 30},
    "Sunny": {"alarm": 0, "speed": None}  # No speed limit change for Sunny
}


# This function simulates a Vehicle Response System (VRS) that reacts to weather conditions.
def vehicleResponseSystem():
    if weatherAlert in weather_responses:
        response = weather_responses[weatherAlert]
        if response["alarm"] > 0:
            print(f"\nThe National Weather Service has updated our alarm by {response['alarm']} minutes because"
                  f" of the forecast of {weatherAlert} weather conditions.")
        else:
            print(f"The National Weather Service is calling for {weatherAlert} skies, drive carefully!")

        sleep(1)
        if response["speed"]:
            print(f"\nVRS System has been engaged only allowing you to drive {response['speed']}mph.")
        else:
            print("\nVRS System has been disengaged")
    else:
        print("Unknown weather condition!")


# Call the function to run the VRS system based on the weather.
vehicleResponseSystem()