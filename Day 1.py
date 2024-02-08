# Day 1 Challenge:
# Create a program that swaps the values of two variables.

# Initialise two variables
variable_one = input("Enter a value for variable one: ")
variable_two = input("Enter a value for variable two: ")

# Confirm the two variables and their values to the user
print(f'''
Your value for variable one is {variable_one}
Your value for variable two is {variable_two}
''')

print('Swapping values...')

# Swap the values of the variables with one another
variable_one, variable_two = variable_two, variable_one

# Print the swapped values of the variables
print(f'''
Your value for variable one is now {variable_one}
Your value for variable two is now {variable_two}
''')
