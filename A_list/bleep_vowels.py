# Write a function `bleep_vowels(text)` that accepts a string and returns
# a new string where all vowels (a, e, i, o, u) are replaced with '*'.

def bleep_vowels(text):
    new_string = ""
    vowels= "aeiou"
    for i in text:
        if i in vowels:
            i = "*"
        new_string += i
    print(new_string)        
# Example:
bleep_vowels("skateboard") #-> 'sk*t*b**rd'
bleep_vowels("slipper") #-> 'sl*pp*r'
bleep_vowels("range") #-> 'r*ng*'
bleep_vowels("brisk morning") #-> 'br*sk m*rn*ng'

