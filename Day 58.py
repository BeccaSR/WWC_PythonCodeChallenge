# Day 58 Challenge:
# Create a function that converts a string to an integer and handles ValueError.

def str_to_int():
    '''
    This function does not take an argument.

    When called, it will ask the user to input an integer.
    It will then convert the string into an integer.

    If the input has not been given in digits, the try-except
    catches the ValueError and asks the user to enter digits.
    The user will be asked again to enter an integer.
    '''
    while True:
        string = input('Please enter a whole number: ')

        try:
            integer = int(string)
            print('String converted')
            return integer
        
        except ValueError:
            print('The value entered cannot be converted, please use digits')

# Call the function            
str_to_int()