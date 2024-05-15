# Day 46 Challenge:
# Write a function to check if a given list is sorted.

def sorted_list(list):
    '''
    This function takes a list as its argument.

    The list is compared with the sorted version
    of the same list.

    If the lists match, the function returns the 
    sentence 'The list is sorted.'

    If the lists do not match,
    'The list is not sorted.' is printed.
    '''
    if list == sorted(list):
        print('The list is sorted.')
    else:
        print('The list is not sorted.')

# initialising lists to check
list1 = [3, 6, 7, 8, 9]
list2 = [4, 2, 6, 1, 7]

# calling the function with the lists
print('\nChecking list 1:')
sorted_list(list1)
print('\nChecking list 2:')
sorted_list(list2)