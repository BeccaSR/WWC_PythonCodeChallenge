# Day 19 Challenge:
# Write a function to calculate the factorial of a number.

# example: factorial of 5 = 5*4*3*2*1
# recursive function will allow this to be calculated

def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

while True:
    # initialise number with user input
    number = int(input("Enter the number you wish to find the factorial of: "))

    # if-else statement to ensure correct input (positive number), and correct answer for 0
    # if number is more than 0, factorial function called with user number as argument
    if number < 0:
        print("Please enter a positive number.")
        continue
    elif number == 0:
        print("The factorial of 0 is 1")
        break
    else:
        print(f"The factorial of {number} is {factorial(number)}")
        break