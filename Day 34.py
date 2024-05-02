# Day 34 Challenge:
# Write a Python program to merge two dictionaries.

dict1 = {"apple" : 3, "banana" : 2}
dict2 = {"carrots" : 4, "dragonfruit" : 2}

def merge_dict(dict1, dict2):
    return(dict1.update(dict2))

merge_dict(dict1, dict2)
print(dict1)