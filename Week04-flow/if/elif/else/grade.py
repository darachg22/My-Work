#Author: Darach Gorham
#Write a program (grade.py) that reads in a student’s percentage mark and prints out corresponding the grade (the program should check that the percentage is valid
#Modified to round float percentage to nearest digit.  
import math

percentage = float(input("Enter the percentage: "))
rounded = round(percentage)

if rounded < 0 or rounded > 100:

 print ("Please enter a number between 0 and 100")
elif rounded < 40: 
 print ("Fail")

elif rounded < 50: 
 print ("Pass")

elif rounded < 60: 
 print ("Merit1")

elif rounded < 70:
 print ("Merit2")

else: 
 print ("Distinction")