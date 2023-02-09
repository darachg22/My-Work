# A random number generator
# Author: Darach Gorham
# I added a second random number to further accustom myself to this task

import random

#number = random.randint(1,56)
#number2 = random.randint(1,56)
#print ('Here is a random number {}'.format(number) )
#print ('Here is a second random number {}'.format(number2) )

#try modifying the program so that the user inputs the range

x = int(input("Enter first number in range: "))
y = int(input("Enter second number in range: "))
print(random.randrange(x, y))
