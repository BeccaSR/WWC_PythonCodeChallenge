# Day 21 Challenge:
# Create a program to remove a specific element from a set.

# initialise my_set variable
my_set = {'apples', 'bananas', 'carrots', 'dates', 'elderberries', 'fennel'}

while True:
    try:
        print(f'The items in the set are: {my_set}')

        # ask user for the element they wish to remove
        element = input("Enter the element you wish to remove: ")

        # use remove() on set, with user element as argument
        my_set.remove(element)

        print(f'The items in the set are now: {my_set}')

        break

    except KeyError:
        # discard() gives error if selected error not in set
        # print custom message in this situation
        print("Your chosen element is not in the set.")
        continue