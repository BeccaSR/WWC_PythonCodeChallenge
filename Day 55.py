# Day 55 Challenge:
# Create a function that takes a string and returns the reverse of each word.

def word_reverse(string):
    '''
    This function takes a string as its input, converted to lowercase.
    The string is split whitespace into a list of words.

    For each word in the list, a for loop iterates backwards through the word
    and checks if each character is a letter.
    If the character is a letter, it is added to the string 'reverse'.
    At the end of the for loop through the word, the reverse word is appended to
    the reversed_words list.

    The function then joins the words in the reversed_words list, with a space
    between them to create the new string - reversed_string.
    '''
    word_list = string.split(' ')
    reversed_words = []

    for word in word_list:
        reverse = ''
        for char in word[::-1]:
            if char.isalpha():
                reverse += char
        reversed_words.append(reverse)

    reversed_string = " ".join(reversed_words)

    return reversed_string

# Initialise string through user input
string = input('Enter a phrase to reverse each word: ').lower()

# Call the function
print(word_reverse(string))