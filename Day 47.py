# Day 47 Challenge:
# Create a program that imports the math module and uses its functions.

import math

num1 = int(input('Enter one integer: '))
num2 = int(input('Enter a second integer: '))

print(f'The square root of {num1} is {math.sqrt(num1)}')
print(f'{num2} to the power of {num1} is {math.pow(num2, num1)}')
print(f'The area of a circle with radius {num1} is {math.pi*(num1**2)}')
print(f'The circumference of a circle with radius {num2} is {math.pi*num2}')