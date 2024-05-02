# Day 36 Challenge:
# Write a Python program to check if two strings are anagrams.

# Ask the user to enter two strings to check, converted to lower case
string1 = input("Enter the first string: ").lower()
string2 = input("Enter the second string: ").lower()

# letters1 dictionary to store how many of each letter is in string1
letters1 = {"a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0,
            "h" : 0, "i" : 0, "j" : 0, "k" : 0, "l" : 0, "m" : 0, "n" : 0,
            "o" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0,
            "v" : 0, "w" : 0, "x" :0, "y" : 0, "z" : 0}

# for loop to count the number of each letter in string1, ignores non-alpha characters
for letter in string1:
    if letter.isalpha():
        letters1[letter] += 1

# letters2 dictionary to store how many of each letter is in string2
letters2 = {"a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0,
            "h" : 0, "i" : 0, "j" : 0, "k" : 0, "l" : 0, "m" : 0, "n" : 0,
            "o" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0,
            "v" : 0, "w" : 0, "x" :0, "y" : 0, "z" : 0}

# for loop to count the number of each letter in string2, ignores non-alpha characters
for letter in string2:
    if letter.isalpha():
        letters2[letter] += 1

# if statement compares if letters1 and letters2 match, if so the strings are anagrams
if letters1 == letters2:
    print(f"'{string1}' and '{string2}' are anagrams")
else:
    print(f"'{string1}' and '{string2}' are not anagrams")