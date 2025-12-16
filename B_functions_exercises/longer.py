# Write a function `longer` that accepts two strings.
# Return the string that is longer.
# If both strings have the same length, return the first string.

def longer(word_1, word_2):
    if len(word_1) > len(word_2):
        print(word_1)
        return word_1
    
    elif len(word_2) > len(word_1):
        print(word_2)
        return word_2
    
    else:
        print(word_1)
        return word_1

first_ = input("First word of choice: ")
second_ = input("Second word of choice: ")

longer(first_, second_)


