# Day 3 Challenge:
# Write a function to count the number of vowels in a given string.

# initialise count at 0
# initialise 'vowels' as a list containing the letters to check for
# for loop to iterate through the given string, checks if each letter is a vowel
    # if letter is a vowel, add 1 to the count
# print a statement of how many vowels there are in the string

def vowel_count(string):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    for letter in string:
        if letter in vowels:
            count += 1

    print(f"There are {count} vowels in your string.")

# ask user to provide a string, convert to lower case
string = input("Enter your string to count its vowels: ").lower()

# call function with users string as the given parameter
vowel_count(string)