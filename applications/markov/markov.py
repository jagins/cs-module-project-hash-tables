import random
from random import randrange

def sentenceGen(string):
# Read in all the words in one go
# with open("input.txt") as f:
#     words = f.read()
# TODO: analyze which words can follow other words
    array = string.split()
    dictionary = {}
    
    for i in range(len(array)):
        if array[i] not in dictionary:
            dictionary[array[i]] = array[i + 1]
    
    values = list(dictionary.values())
    number = randrange(len(dictionary))
    j = 0
    new_string = ''
    while j != len(dictionary):
        new_string = new_string + ' ' + values[number]
        number += 1
        if number > len(dictionary):
            number = 0
        j += 1
    print(new_string)



# TODO: construct 5 random sentences
# Your code here

string = 'Cats and dogs and birds and fish dogs birds'
sentenceGen(string)