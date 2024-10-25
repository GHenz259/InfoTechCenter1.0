import sys  # Import the sys module for system-specific parameters and functions
import time  # Import the time module to use sleep function for delays
import random
from time import sleep

# Print a welcome message
print("\nWelcome to InfoTechCenter V1.0\n")

timeToSleep = 3 #variable to set the time library to 3 seconds when called
time.sleep(timeToSleep) # Calling the time to sleep library with the variable timeToSleep's value

# Initialize variables
x = 0  # Counter for the booting process
ellipsis = 0  # Variable to track the number of dots in the message

# Loop until the booting process reaches 20 iterations
while x != 20:
    x += 1  # Increment the boot counter
    # Create a message with a dynamic number of dots based on 'ellipsis'
    message = ("InfoTech Center System Booting" + "." * ellipsis)
    ellipsis += 1  # Increment the ellipsis counter
    # Print the message, overwriting the previous line
    sys.stdout.write("\r" + message)
    time.sleep(0.5)  # Pause for half a second to simulate boot time
    # Reset ellipsis counter after reaching 4
    if ellipsis == 4:
        ellipsis = 0
    # Print the final message once booting is complete
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted")

print("\n******************************************************\n")

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



# Print a decorative separator for the output
print("\n******************************************************\n")
print("Gasoline Branch\n")


# Function to randomly select a gas level status
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)


# Function to randomly select a gas station
def gasStations():
    gasStationList = ["VP", "Shell", "Meijer", "Sam's Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    return random.choice(gasStationList)


# Function to get distance based on gas level
def getDistance(gas_level):
    if gas_level == "Low":
        return round(random.uniform(1, 25), 1)  # For "Low" level
    elif gas_level == "Quarter Tank":
        return round(random.uniform(25.1, 50), 1)  # For "Quarter Tank"
    return None


# Function to display gas level warnings and information
def gasLevelAlert():
    gasLevelIndicator = gasLevelGauge()

    # Dictionary mapping gas levels to messages and actions
    gasActions = {
        "Empty": ("*** WARNING - YOU ARE ON EMPTY ***\n", "Calling Triple AAA", 2),
        "Low": ("Your gas tank is extremely low, checking GPS for the closest gas station", None, 2),
        "Quarter Tank": ("Your gas tank is a quarter full, checking GPS for the closest gas station", None, 2),
        "Half Tank": ("Your gas tank is half full which is plenty to get to your destination.", None, 0),
        "Three Quarter Tank": ("Your gas tank is three quarters full.", None, 0),
        "Full Tank": ("Your gas tank is full!", None, 0)
    }

    # Get the corresponding message and action for the current gas level
    message, action, delay = gasActions.get(gasLevelIndicator, ("Unknown gas level", None, 0))

    print(message)
    if delay > 0:
        sleep(delay)

    if gasLevelIndicator in ["Low", "Quarter Tank"]:
        distance = getDistance(gasLevelIndicator)
        print(f"The closest gas station is {gasStations()} which is {distance} miles away.")

    if action:
        print(action)


# Execute the program
gasLevelAlert()

