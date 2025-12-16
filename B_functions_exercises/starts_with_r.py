# Write a function `starts_with_r` that accepts a string as an argument.
# The function should return True if the string starts with 'r' or 'R'.
# Otherwise, return False.
# Write a function `starts_with_r` that accepts a string as an argument.
# The function should return True if the string starts with 'r' or 'R'.
# Otherwise, return False.

def starts_with_r(word):
    if word.startswith('r') or word.startswith('R'):
        print('True')
        return True
    else:
        print('False')
        return False

word_ = input("Input a word of your choice: ")

starts_with_r(word_)