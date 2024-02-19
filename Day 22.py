# Day 22 Challenge:
# Create a program to find the second-largest element in a list.

def second_largest(numbers):
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
    number_int.remove(max(number_int))

    # print largest number remaining in list (second largest in original)
    print(f'The second largest number in your list is {max(number_int)}.')


# ask user to enter numbers, call function using the numbers as the argument
numbers = input("Enter your numbers, separated with a comma (,):")
second_largest(numbers)