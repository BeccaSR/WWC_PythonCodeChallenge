# Day 42 Challenge:
# Write a program that uses a try-except block to handle division by zero.

def division(num1, num2):
    '''
    This function takes two integers as its arguments.

    It then divides the first number by the second and returns the output.

    If the divisor is 0, the try-except handles the zero division error.
    '''
    try:
        print(f'{num1} / {num2} = {(num1/num2)}')

    except ZeroDivisionError:
        print('Unable to divide by zero, please try again.')

number1 = int(input('Enter the dividend: '))
number2 = int(input('Enter the divisor: '))

division(number1, number2)