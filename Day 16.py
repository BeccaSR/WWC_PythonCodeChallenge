# Day 16 Challenge:
# Write a function that counts the frequency of each word in a sentence.

def word_frequency(string):
    # split the string into a list of words
    word_list = string.split()

    # create empty dictionary to store word frequencies
    word_freq = {}

    # loop through the word list
    # if word not in word_freq dictionary, add to dictionary with value of 1
    # if word in dictionary, increase value by 1
    for word in word_list:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1
    
    # loop through dictionary to print words and their frequency count
    for keys, values in word_freq.items():
        print(f"The word '{keys}' appeared {values} times.")


string = input("Enter your sentence: ")

word_frequency(string)