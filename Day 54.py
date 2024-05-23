# Day 54 Challenge:
# Create a function to find all words in a sentence that start with a vowel.

def find_vowels(string):
    '''
    This function takes a string as its input.
    The string is split into a list of words.

    The for loop then checks the first letter of each word.
    If the letter is in the vowel list, vowel_count is increased by 1.
    The final count of words beginning with a vowel is then printed.
    '''
    word_list = string.split(' ')
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0

    for word in word_list:
        if word[0] in vowels:
            vowel_count += 1

    print(f'{vowel_count} words begin with a vowel.')

# Initialise string through user input
string = input('Enter a phrase to see how many words begin with a vowel: ').lower()

# Call the function
find_vowels(string)