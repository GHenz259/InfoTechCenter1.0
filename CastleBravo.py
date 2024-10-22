# Print a decorative separator for the output
print("\n******************************************************\n")

# Print the branch title
print("Gasoline Branch\n")

# Importing the random module to generate random values
import random
# Importing sleep from time module to add delay in the output
from time import sleep


# Function to randomly select a gas level status
def gasLevelGauge():
    # List of possible gas levels
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    # Randomly choose and return a gas level
    return random.choice(gasLevelList)


# Function to randomly select a gas station
def gasStations():
    # List of possible gas station names
    gasStationList = ["VP", "Shell", "Meijer", "Sam's Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    # Randomly choose and return a gas station name
    return random.choice(gasStationList)


# Function to display gas level warnings and information
def gasLevelAlert():
    # Randomly generate distances to the nearest gas station for low and quarter tank situations
    milesToGasStationLow = round(random.uniform(1, 25), 1)  # Random distance between 1 and 25 miles
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50), 1)  # Random distance between 25.1 and 50 miles
    # Get the current gas level status
    gasLevelIndicator = gasLevelGauge()

    # Check the gas level and provide corresponding messages
    if gasLevelIndicator == "Empty":
        print("*** WARNING - YOU ARE ON EMPTY ***\n")
        # Pause for 2 seconds before the next action
        sleep(2)
        # Suggest calling for roadside assistance
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking GPS for the closest gas station")
        sleep(2)
        # Display the nearest gas station and distance
        print("The closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is a quarter full, checking GPS for the closest gas station")
        sleep(2)
        # Display the nearest gas station and distance
        print("The closest gas station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        # Inform the user that there's enough gas to reach the destination
        print("Your gas tank is half full which is plenty to get to your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        # Inform the user about the gas level
        print("Your gas tank is three quarters full.")
    else:
        # Inform the user that the tank is full
        print("Your gas tank is full!")


# Call the gasLevelAlert function to execute the program
gasLevelAlert()