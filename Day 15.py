# Day 15 Challenge:
# Create a program that checks if a year is a leap year.

# function to check if a year is a leap checks if year is evenly divisible by 4
# if so, the function checks if it is evenly dvisible by 100
# if so, the function checks if it is evenly dvisible by 400
# the function then return whether or not the year is a leap year

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year!")
            else:
                print(f"{year} is not a leap year!")
        else:
            print(f"{year} is a leap year!")
    else:
        print(f"{year} is not a leap year!")


while True:
    try:
        # initialise year variable through user input
        year = int(input("Enter the year you wish to check: "))

        # check length of input is 4
        if len(str(year)) != 4:
            print("Please enter the year as a four digit number")
            continue
        else:
            # call the function
            leap_year(year)

            break
    
    # except statement for non-integer input
    except ValueError:
        print("Please enter the year as a four digit number")
        continue