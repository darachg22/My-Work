# it takes in a float amount of dollars and returns that absolute amount in cent.
# Author Darach Gorham
# I used the absolute.py formula and tweaked it by multipying the number by 100 and then converting it to an integer on line 9.

import math

number = float(input("Enter amount:"))

absoluteValue = abs ((number*100))

print ('This amount in cent is {}c '.format (int(absoluteValue)))