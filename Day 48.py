# Day 48 Challenge:
# Create a program that replaces specific words in a text with their synonyms.

from nltk.corpus import wordnet
import random

def replace_synonym(text, word):
    
    synonyms = []

    for syn in wordnet.synsets(word):
        for i in syn.lemmas():
            synonyms.append(i.name())

    text = text.replace(word, random.choice(synonyms))
    print(text)

text = input('Enter your phrase: ').lower()
word = input('Enter the word in your phrase you wish to change to a synonym: ').lower()

replace_synonym(text, word)