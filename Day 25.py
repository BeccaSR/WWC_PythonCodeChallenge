# Day 25 Challenge:
# Create a program to concatenate two lists.

# initialise two list variables
list_one = ['apple', 'banana', 'carrot', 'dragonfruit']

list_two = [34, 42, 61, 14]

# use extend() method to add list two onto the end of list one
list_one.extend(list_two)

# print extended list
print(list_one)