# Day 39 Challenge:
# Write a program to find the most common words in a text file.

from collections import Counter 

def find_common_words(file_name):
    '''
    This function takes the name of a text file as its argument.
    The file is then opened and the text split into 
    individual words converted to lowercase.

    The Counter module is then used to find the 10 most common words.

    The function the prints the 10 most common words, and the count.
    '''
    file = open(file_name, "r")
    words = file.read().lower().split()
    
    most_common = Counter(words).most_common(10)

    print(
    f'''The 10 most common words are:
        {most_common}'''
    )


# Test the function
find_common_words("text.txt")