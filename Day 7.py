# Day 7 Challenge:
# Write a program to check if a number is positive, negative, or zero.

# try except block for valueError of user not entering number as digits
while True:
    try:

        number = int(input('Enter a number: '))

        # if-else statement to compare entered number to zero
        if number > 0:
            print('Your number is positive!')
            break
        elif number < 0:
            print('Your number is negative!')
            break
        else:
            print('Your number is zero!')
            break
    
    # if valueError, while loop continues and user prompted to re-enter number
    except ValueError:
        print('Please enter your number in digits.')
        continue