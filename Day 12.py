# Day 12 Challenge:
# Write a program to reverse a given string.

# initialise string with user input
string = input("Enter a string to be reversed: ")
print("Reversing string...")

# initialise an empty to string to enter reversed string into
reversed_string = ""

# iterate in reverse through each character of the string
# add the character to the reversed_string character
for char in string[::-1]:
    reversed_string += char

# print statement to return reversed string
print("Your reversed string is: ")
print(reversed_string)