# Day 30 Challenge:
# Create a function that finds the second smallest element in a list.

def second_smallest(numbers):
    # split values in numbers, using ',' as the delimiter
    number_list = numbers.split(',')

    # initialise empty list to hold values as integers
    number_int = []

    # for loop for each value in list
        # remove any whitespace
        # convert string to integer and append to number_int list
    for number in number_list:
    
        num = number.strip()
        number_int.append(int(num))

    # remove largest number from number_int list
    number_int.remove(min(number_int))

    # print largest number remaining in list (second largest in original)
    print(f'The second smallest number in your list is {min(number_int)}.')


# ask user to enter numbers, call function using the numbers as the argument
numbers = input("Enter your numbers, separated with a comma (,):")
second_smallest(numbers)