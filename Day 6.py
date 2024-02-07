# Day 6 Challenge:
# Write a program to count the occurrences of a specific character in a string.

# define variable to take two parameters - user string, chosen character
# initialise count at 0
# for loop to iterate through the given string, checks if letter matches selection
    # if letter matches user selection, add 1 to the count
# print a statement of how many times the chosen character appears

def letter_count(string, character):
    count = 0
    
    for letter in string:
        if letter == character:
            count += 1

    print(f"The character '{character}' appears {count} times in your string.")

# ask user to provide a string and chosen character, convert to lower case
string = input("Enter your string: ").lower()
character = input("Enter the character you wish to count the occurances of: ").lower()

# call function with users string and chosen character as the given parameters
letter_count(string, character)