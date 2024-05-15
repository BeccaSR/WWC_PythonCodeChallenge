# Day 44 Challenge:
# Write a program that reads an integer from the user and handles invalid inputs.

# try-except block returns an error when a non-integer value is entered
# the while loop allows the user to try again, without having to rerun the program
while True:

    integer = input('Please enter an integer: ')

    try:
        print(f'You have entered the integer {int(integer)}.')
        break

    except ValueError:
        print('You have not entered an integer, please try again.')
        continue