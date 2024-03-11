# Day 30 Challenge:
# Create a function that finds the second smallest element in a list.

def second_smallest(numbers):
    '''
    This function takes in a string consisting of comma separated numbers,
    it returns the second smallest element in the list.

    The string is split, and a for loop is used to remove any whitespace
    before converting each number into an integer.

    The smallest number is removed from the number_int list.
    Finally, a print statement is returned stating the smallest number
    remaining from the list.
    '''
    number_list = numbers.split(',')

    number_int = []

    for number in number_list:
    
        num = number.strip()
        number_int.append(int(num))

    number_int.remove(min(number_int))

    print(f'The second smallest number in your list is {min(number_int)}.')


# ask user to enter numbers, call function using the numbers as the argument
numbers = input("Enter your numbers, separated with a comma (,):")
second_smallest(numbers)