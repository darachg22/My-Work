#Author: Darach Gorham
#Modified to only accept -1

numbertoinput = -1

number = int (input("enter an integer:"))

while number != numbertoinput:

    number = int (input("enter an integer:"))
    
    if (number % 2) == 0:
        print (f"{number} is an even number")
    else:
        print (f"{number} is an odd number")

