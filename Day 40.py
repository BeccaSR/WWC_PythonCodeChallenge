# Day 40 Challenge:
# Write a function to find the largest common divisor of two numbers using a function.

import math

def find_hcm(num1, num2):
    '''
    This function takes two integers as its arguments.

    The gcd module is then used to return the hcm of the numbers.
    '''
    
    print(f'The largest common divisor of {num1} and {num2} is {math.gcd(num1, num2)}')

number1 = int(input('Enter a number: '))
number2 = int(input('Enter a second number: '))

find_hcm(number1, number2)