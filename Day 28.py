# Day 28 Challenge:
# Create a program that removes the nth element from a list.

my_list = ['oranges', 'grapefruit', 'lemon', 'lime', 'kiwi']

while True:
    print(f'''
Your current list is:
    {my_list}''')
    
    # ask user to state the number (not index) of the item they want to remove
    remove = int(input('Enter the number of the item you wish to remove: '))

    # check number given has a corresponding item
    # if not, give error message and continue while loop
    if remove > len(my_list) or remove <= 0:
        print('The number you have entered does not have a corresponding item.')
        continue

    # if number is correct, remove item from list and print new list
    # exit while loop
    else:
        del my_list[remove - 1]
        print(f'''
Item {remove} removed. Your new list is:
    {my_list}''')
        break

