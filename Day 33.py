# Day 33 Challenge:
# Write a test case for a function that checks if a number is prime.

# Define function that identifies prime numbers
def is_prime(number):
    """
    This function takes an integer as its argument
    If the integer is equal to or less than one, it will return false.
    Otherwise, it will see if the modulus of the integer and a value (i) is 0
    If 0, it will return false.
    i ranges from 2 to the square root of the given integer.
    If there is no modulus of 0 found, the integer is prime
    and the function returns true.
    """

    if int(number) <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if int(number) % i == 0:
            return False
    return True


# Test the function
# Dictionary contains a number and flase/true identifier
# Iterate through number list, and compare outcome to dictionary identifier
# Break loop if function incorrect
numbers = { 18 : False, 1 : False, 64 : False, 37 : True, 17 : True}

for num in numbers:
    if is_prime(num) == numbers[num]:
        print(f"{num} identified correctly")
    else:
        print(f"{num} identified incorrectly")
        break