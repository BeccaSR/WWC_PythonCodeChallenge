# Day 51 Challenge:
# Create a program that counts the occurrences of each word in a text file.

def count_words(file_name):
    '''
    This function takes the name of a text file as its argument.
    The file is then opened and the text split into 
    individual words converted to lowercase.

    The for loop checks if each word exists in the word_count dictionary.
    If it does, the value for the word is increased by 1.
    If not, the word is added to the dictionary with a value of 1.
    '''
    file = open(file_name, "r")
    words = file.read().lower().split()

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] + 1

    print(word_count)
    

# Test the function
count_words("text.txt")