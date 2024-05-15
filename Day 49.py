# Day 49 Challenge:
# Create a program that implements the bubble sort algorithm.

'''
The bubble sort algorithm sorts numbers into ascending order
by comparing two consecutive values in the list, and swapping 
them if the second number is smaller than the first.
This continues until each pair of numbers is checked and there
are no swaps needed.
'''
def bubble_sort(list):
    '''
    This function takes a list of numbers as its argument.

    It iterates through the list, comparing the value at i
    with each value at j. If i is bigger than j, the values
    switch positions in the list.

    The function returns the list in ascending order.
    '''
    for i in range(0, len(list)-1):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

print(bubble_sort([3,2,6,1,7]))