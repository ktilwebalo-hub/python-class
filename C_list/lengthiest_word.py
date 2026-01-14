# Write a function `lengthiest_word(sentence)` that accepts a string containing a sentence.
# The function should return the longest word in the sentence.
# If there is a tie, return the word that appears later in the sentence.

def lengthiest_word(sentence):
    new_list = sentence.split(" ")
    words = ""
    for i in new_list:
        if len(i) >= len(words):
            words = i
    print(words)
# Example:
lengthiest_word("I am pretty hungry") #-> 'hungry'
lengthiest_word("we should think outside of the box") #-> 'outside'
lengthiest_word("down the rabbit hole") #-> 'rabbit'
lengthiest_word("simmer down") #-> 'simmer'

