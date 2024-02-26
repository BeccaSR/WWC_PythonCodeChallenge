# Day 26 Challenge:
# Create a program that uses a lambda function to square each element of a list.

# initialise list with integers
my_list = [2, 5, 74, 16, 32]

# lambda function with for loop to print each number in list squared
square = lambda my_list: [print(f'{num} squared = {num ** 2}') for num in my_list]

# call lambda function, with list as argument
square(my_list)