# Write a function `remove_vowels(s)` that accepts a string and returns a new string
# with all vowels removed (a, e, i, o, u).

def remove_vowels(s):
    str = ""
    char = ""
    vowels = "aeiou"
    for i in range(len(s)):
        char = s[i]
        if char not in vowels:
            str += char
                     
    return str
# Example usage:
print(remove_vowels("jello"))  # 'jll'
print(remove_vowels("sensitivity"))  # 'snstvty'
print(remove_vowels("cellar door"))  # 'cllr dr'

