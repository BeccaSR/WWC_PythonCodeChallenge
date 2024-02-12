# Day 13 Challenge:
# Write a program to shuffle the elements of a list randomly.

import random

# initialise list of items
my_list = ['apples', 'bananas', 'carrots', 'dates', 'elderberries', 'fennel', 'grapes']

# use shuffle() method on list
random.shuffle(my_list)

# print newly shuffled list
print(my_list)