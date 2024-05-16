# Day 52 Challenge:
# Create a program that checks if a string is a palindrome.

def is_palindrome(string):
    '''
    This function takes a string as its input.
    Whitespace is removed and a for loop creates a reversed version.

    The function then compares the original string (no whitespace)
    with the reversed version.

    If they match, the string is a palindrome.
    '''
    string = string.replace(' ', '')
    reverse_string = ''

    for letter in reversed(string):
        reverse_string += letter

    if string == reverse_string:
        print('This is a palindrome.')
    else:
        print('This is not a palindrome.')

# Initialise string through user input
string = input('Enter a phrase to see if it is a plaindrome: ').lower()

# Call the function
is_palindrome(string)