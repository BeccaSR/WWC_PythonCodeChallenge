# Day 38 Challenge:
# Write a program to flatten a nested list.

nested_list = [["apple", "banana", "carrot"], ["coffee", "tea", "water"]]

def flatten_list(list):
    flat_list = []
    for item in list:
        flat_list.extend(item)
    return flat_list

print(f"Nested list: {nested_list}")
print(f"Flattened list: {flatten_list(nested_list)}")