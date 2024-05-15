# Day 43 Challenge:
# Write a program that removes all whitespaces from a given string.

def remove_whitespace(string):
    """
    This function takes a user inputted string as an argument.

    It then returns the string with any whitespace removed.
    """
    print(f'The string "{string}" with all whitespace removed is:')
    print(f'{string.replace(' ', '')}')

sentence = input('Enter your sentence to remove whitespace from: ')

remove_whitespace(sentence)
