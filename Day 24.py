# Day 24 Challenge:
# Write a program to remove vowels from a given string.

def remove_vowels(string):

    # list containing vowels for for loop to check for
    vowels = ['a', 'e', 'i', 'o', 'u']
    # initialise empty string for use in for loop
    no_vowels= ''

    # for loop to check if each character in the string is a vowel
    # if character is not a vowel (not in vowel list), 
        # append this to no_vowels string
    for char in string:
        if char.lower() not in vowels:
            no_vowels += char

    # print statement to return string with vowels removed
    print('Your string without vowels is:')
    print(no_vowels)

# ask user to input string, call function with user string as argument
string = input('Please enter your string: ')
remove_vowels(string)