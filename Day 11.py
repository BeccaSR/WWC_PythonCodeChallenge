# Day 11 Challenge:
# Write a program to print the multiplication table of a given number.


# try except block for valueError of user not entering number as digits
while True:
    try:

        # initialise number with users choice of number
        number = int(input("Enter the number you would like the multiplication table of: "))

        # for loop running from i = 0 to i = 12, printing multiplication and answer
        for i in range(0, 13):
            print(f"{i} x {number} = {i * number}")
        break
    
    # if valueError, while loop continues and user prompted to re-enter number
    except ValueError:
        print('Please enter your number in digits.')
        continue