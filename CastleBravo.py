import sys
import time

print("\nWelcome to InfoTechCenter V1.0\n")


x=0
ellipsis=0

while x != 20:
    x += 1
    message=("InfoTech Center System Booting" + "." * ellipsis)
    ellipsis += 1
    sys.stdout.write("\r" + message)
    time.sleep(0.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted")