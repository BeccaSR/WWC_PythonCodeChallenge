# Day 57 Challenge:
# Create a function that returns the key with the maximum value in a dictionary.

def max_value(dict):
    '''
    This function takes a dictionary as its argument.

    It then finds the largest value in the dictionary, 
    and returns the key with this value.
    '''
    max_value_key = (max(dict, key=dict.get))

    print(f'The key with the largest value is "{max_value_key}"')

# Initialise a dictionary
dictionary = {"apple" : 3, "banana" : 2, "carrots" : 4, "dragonfruit" : 2}

# Call the function
max_value(dictionary)