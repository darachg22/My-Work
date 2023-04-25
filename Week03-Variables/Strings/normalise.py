# A Program that Normalises a sentence
#Author: Darach Gorham
#My attempt before checking example

#string = input( "input string: ")
#StrWoCaps = str.casefold(string) 
#lengthOfstring = len (string)
#print (StrWoCaps)
#print (f'The length of string is {lengthOfstring}' )

rawString = input("please enter a string:")
normalisedString = rawString.strip().lower()
lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)
print(f"That String normalised is :{normalisedString}")
print(f"we reduced the input string from {lenghtOfRawString} to {lenghtOfNormalised} characters") 