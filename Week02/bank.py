# Bank.py 
# This program takes number in cents and converts them to euro with a decimel place.
# Author: Darach Gorham

# Adding two numbers resource used: https://www.w3schools.com/python/python_howto_add_two_numbers.asp 
# Float resource used: https://careerkarma.com/blog/python-float/#:~:text=The%20float()%20method%20is,to%20a%20floating%2Dpoint%20value.&text=The%20float()%20method%20takes,its%20default%20value%20is%200.0.


x= input ('Enter amount 1 (in cent):')

y= input ('Enter amount 2 (in cent):')

sum = (int(x) + int(y))/100

print ("€", (sum))
