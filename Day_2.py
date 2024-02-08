# Day 2 Challenge:
# Create a program to calculate the area of a circle given its radius.

import math

# Define function that calculates the area of a circle,
# taking radius as the parameter
def circle_area(radius):
    area = math.pi * radius * radius
    print(f"The area of a circle with radius {radius} is {area:.2f} (to 2dp)")

# Ask the user to enter the radius
radius = int(input("Enter the radius of the circle: "))

# Call circle_area function with user's radius as parameter
circle_area(radius)
