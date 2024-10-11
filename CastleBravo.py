import sys  # Import the sys module for system-specific parameters and functions
import time  # Import the time module to use sleep function for delays

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
