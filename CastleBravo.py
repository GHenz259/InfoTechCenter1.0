import random
from time import sleep

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