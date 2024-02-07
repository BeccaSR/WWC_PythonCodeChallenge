# Day 8 Challenge:
# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

# initialise upper and lower variables at 0
# for loop to iterate through the given string, 
    # checking the ASCII code to ascertain if uppercase or lowercase
    # if letter is uppercase, increase upper by 1
    # if letter is lowercase, increase lower by 1
# print a statement of how many upper and lowercase letters the string contains

def upper_lower_count():
    user_string = input("Please enter your string: ")

    upper = 0
    lower = 0

    for char in user_string:
        if ord(char) >= 65 and ord(char) <= 90:
            upper += 1
        elif ord(char) >= 97 and ord(char) <= 122:
            lower += 1

    print(f"Your string contains {upper} uppercase and {lower} lowercase letters.")

# call the function
upper_lower_count()
