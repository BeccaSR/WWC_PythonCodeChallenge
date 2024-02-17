# Day 20 Challenge:
# Write a function that takes a list of numbers and returns a new list containing only the even numbers.


def evens(numbers):
    # split values in numbers, using ',' as the delimiter
    number_list = numbers.split(',')

    # initialise two empty lists - one to hold original values as integers
    # second list for the even values
    original_numbers = []
    even_numbers = []

    # for loop for each value in list
        # remove any whitespace
        # convert string to integer and append to original numbers list
        # check if number is even, if so append to even numbers list
    for number in number_list:
        
        num = number.strip()
        original_numbers.append(int(num))
        
        if int(num) % 2 == 0:
            even_numbers.append(int(num))

    # print statement showing user original list, and even numbers only list
    print(f'Your original list: {original_numbers}')
    print(f'Your list with only even numbers {even_numbers}')

# ask user to enter numbers, call function using the numbers as the argument
numbers = input("Enter your numbers, separated with a comma (,):")
evens(numbers)