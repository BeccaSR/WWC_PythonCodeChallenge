# Day 59 Challenge:
# Create a function that checks if a number is a perfect square.

import math

def check_square(number):
    square_root = math.sqrt(number)

    if square_root.is_integer():
        print(f'{number} is a perfect square. It has a square root of {square_root}.')

    else:
        print(f'{number} is not a perfect square. It has a square root of {square_root}.')

# Initialise a number
num = int(input('Enter an integer to check if it is a perfect square number: '))

# Call the function
check_square(num)