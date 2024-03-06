# Day 32 Challenge:
# Create a function that calculates the average of a list of numbers.

def calculate_average(numbers):
    """
    This function will take a string of comma separated numbers as its argument
    It will convert the numbers to a list, then run a for loop to remove whitespace
    and convert the string to an float, adding this to a 'number_float' list.

    The function then calculates the average value of the list (sum divided by length)
    and returns a print statement with the average.
    """
    
    number_list = numbers.split(',')

    number_float = []

    for number in number_list:
    
        num = number.strip()
        number_float.append(float(num))

    average = sum(number_float) / len(number_float)

    print(f'The average of your list is {average}.')


# ask user to enter numbers, call function using the numbers as the argument
numbers = input("Enter the numbers you wish to find the average of, separated with a comma (,):")
calculate_average(numbers)