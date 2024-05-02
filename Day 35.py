# Day 35 Challenge:
# Write a simple unit test for a function that adds two numbers.

# Define function that adds two numbers and returns the output
def add_two_numbers(num1, num2):
    return int(num1) + int(num2)

# Test the function
# Each set contains 3 values - the thrid value is the expected output
# when the first and second value are added together
test1 = (1, 5, 6)
test2 = (34, 52, 86)
test3 = (-5, 9, 4)

if add_two_numbers(test1[0], test1[1]) == test1[2]:
    print("test1 correct")
else:
    print("test1 incorrect")

if add_two_numbers(test2[0], test2[1]) == test2[2]:
    print("test2 correct")
else:
    print("test2 incorrect")

if add_two_numbers(test3[0], test3[1]) == test3[2]:
    print("test3 correct")
else:
    print("test3 incorrect")
