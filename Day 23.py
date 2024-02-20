# Day 23 Challenge:
# Write a program that checks if a key exists in a dictionary.

# initialise dictionary with key:value pairs
my_dict = {'apples' : 4,
           'bananas' : 7,
           'carrots' : 15,
           'dates' : 30,
           'elderberries' : 49,
           'fennel' : 5,
           'grapes' : 12}

# ask user for key they wish to check for
key_check = input("Enter the key you wish to check for: ")

# check if lowercase version of key is in dictionary, returning its value if it is
# if not, print statement to say it is not in the dictionary
if key_check.lower() in my_dict:
    print(
f'''The key {key_check} is in the dictionary, it's value is {my_dict[key_check.lower()]}''')
else:
    print(f'The key {key_check} is not in the dictionary.')