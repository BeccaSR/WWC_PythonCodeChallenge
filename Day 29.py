# Day 29 Challenge:
# Create a function that generates a random number between a given range.

import random

while True:

    lowest_num = int(input('Enter the lowest number you wish to use: '))
    highest_num = int(input('Enter the highest number you wish to use: '))

    if lowest_num >= highest_num:
        print('Make sure your second number is bigger than the first number.')
        continue

    else:
        print(f'Generating random number between {lowest_num} and {highest_num}')
        print(random.randrange(lowest_num,highest_num+1))
        break