# Day 9 Challenge:
# Write a program to check if a number is even or odd.

# try except block for valueError of user not entering number as digits
while True:
    try:

        number = int(input('Enter a number: '))

        # if-else statement to determine if number odd or even, using modulus
        if number % 2 == 0:
            print('Your number is even!')
            break
        else:
            print('Your number is odd!')
            break
    
    # if valueError, while loop continues and user prompted to re-enter number
    except ValueError:
        print('Please enter your number in digits.')
        continue