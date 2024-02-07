# Day 4 Challenge:
# Write a program to find the sum of all elements in a list.

# initialise a list with integers as the elements
my_list = [3, 5, 58, 7, 12, 45, 12, 6]

# initialise sum at 0
# for each value in the list, add the value to 'sum'
sum = 0

for value in my_list:
    sum += value

# return the sum of the elements
print(f"The sum of the elements in the list is {sum}.")