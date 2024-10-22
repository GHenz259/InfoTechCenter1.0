print("\n******************************************************\n")

print("Gasoline Branch\n")

import random
from time import sleep

def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

def gasStations():
    gasStationList = ["VP", "Shell", "Meijer", "Sam's Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    return random.choice(gasStationList)

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("*** WARNING - YOU ARE ON EMPTY ***\n")
        sleep(2)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking GPS for the closest gas station")
        sleep(2)
        print("The closest gas station is",gasStations(),"which is",milesToGasStationLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is a quarter full, checking GPS for the closest gas station")
        sleep(2)
        print("The closest gas station is",gasStations(),"which is",milesToGasStationQuarterTank,"miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is half full which is plenty to get to your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three quarters full.")
    else:
        print("Your gas tank is full!")

gasLevelAlert()