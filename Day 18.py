# Day 18 Challenge:
# Create a program to find the largest among three numbers.


while True:
    try:
        # asking user to input the three numbers they wish to use
        number_one = int(input("Enter the first number: "))
        number_two = int(input("Enter the second number: "))
        number_three = int(input("Enter the third number: "))

        # adding the three numbers to a list
        numbers = [number_one, number_two, number_three]

        # using the max() function to return the largest number in the list
        # storing this number in the largest_number variable
        largest_number = max(numbers)

        # print statement to show user the three inputted numbers, and the largest
        print(
f'''The largest number out of {number_one}, {number_two} and {number_three} is:
    {largest_number}''')
        
    except ValueError:
        print('Please enter your number in digits.')