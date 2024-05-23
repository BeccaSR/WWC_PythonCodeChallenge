# Day 41 Challenge:
# Write a program that uses recursion to generate all permutations of a list.

def permute_list(list):
    permutations = []

    if len(list) == 0 or len(list) == 1:
        return list
    else:
        for i, let in enumerate(list):
            for perm in permute_list(list[:i] + list[i+1:]):
                permutations += [let + perm]
    return permutations

print(permute_list(['1','2','3']))


