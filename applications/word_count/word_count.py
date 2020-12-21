import re
from string import punctuation
def word_count(s):
    dictionary = {}

    #bad chars is a set full of puncuation marks
    bad_chars = set(punctuation)
    #remove "'" from the set
    bad_chars.remove("'")

    #convert the string to lower case
    lowercase_string = s.lower()
    
    #clean up the string if if it has special characters
    for word in bad_chars:
        lowercase_string = lowercase_string.replace(word, '')

    #split the string into separate array elements
    new_string = lowercase_string.split()
    
    #loop through the array and check if the word is in the dictionary
    #if it's not put in the dictionary with a value of 1
    #otherwise increase the count
    for word in new_string:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    
    return dictionary

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello!"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('a a\ra\na\ta \t\r\n'))