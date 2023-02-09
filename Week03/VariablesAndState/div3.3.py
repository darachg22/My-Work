#Dividing program that gives remainder
#Author: Darach Gorham


#My code before looking at the answer key
#Used this as reference: https://careerkarma.com/blog/python-modulo/ 

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
print(int(x / y),' with a remainder of', (y % x))

#Example answer given
#x = int(input("Enter first number: "))
#y = int(input("Enter the number you want to divide by: "))
#answer = int(x//y) # // gives the int division
#remainder = x%y # % gives the remainder
#print("{} divided by {} is {} with remainder {}".format( x, y,answer, remainder))
