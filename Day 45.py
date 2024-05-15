# Day 45 Challenge:
# Write a function to check if a number is a prime number.

def is_prime(number):
    """
    This function takes an integer as its argument.
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


number = int(input('Enter a number to check if it is a prime number: '))

if is_prime(number):
    print(f'{number} is a prime number.')
else:
    print(f'{number} is not a prime number.')