# Day 10 Challenge:
# Write a program to remove duplicates from a list.

# initialise a list with duplicated elements
my_list = [2, 5, 2, 5, 3, 6, 3 , 4 , 7, 8, 4, 2, 1]

# initialise empty list
duplicate_free_list = []

# iterate through my_list
    # check duplicate_free_list to see if the item is already in the list
    # if it is not, append the item to the duplicate_free_list
    # it is is, move on to the next item in my_list
for item in my_list:
    if item not in duplicate_free_list:
        duplicate_free_list.append(item)

# print statement to show successful removal of duplications
print(f'''
Your original list:
    {my_list}
Your list without duplicates:
    {duplicate_free_list}
''')