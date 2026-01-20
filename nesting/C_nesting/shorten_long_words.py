# Write a function `shorten_long_words(sentence)` that accepts a string and returns
# the same sentence where words longer than 4 characters have their vowels removed.
def shorten_long_words(sentence):
    sent_ = sentence.split(" ")
    str_ =[]
    vowels = "aeiou"
    for i in sent_:
        if len(i) <= 4:
            str_.append(i)
        else:
            word = remove_vowels(i)
            str_.append(word)
            
    return " ".join(str_)
    
def remove_vowels(s):
    str = ""
    char = ""
    vowels = "aeiou"
    for i in range(len(s)):
        char = s[i]
        if char not in vowels:
            str += char
            
# Example usage:
print(shorten_long_words("they are very noble people"))  # 'they are very nbl ppl'
print(shorten_long_words("stick with it"))  # 'stck with it'
print(shorten_long_words("ballerina, you must have seen her"))  # 'bllrna, you must have seen her'
