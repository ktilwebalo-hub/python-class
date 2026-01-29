#Write a function `letter_map` that accepts:
#- a string
#- a dictionary
#The function should return a new string where characters that appear
#as keys in the dictionary are replaced with their corresponding values.

def letter_map(str, dict):
    new_str = ""
    for i in str:
        if i in dict:
            new_str += dict[i]

        else:
            new_str += i
    return new_str

        
print(letter_map("symbolic", {"y":"i","o":"a","c":"k" }))
# 'simbalik'

print(letter_map("colossal", {"o":"x","s":"p" }))
# 'cxlxppal'

print(letter_map("miniscule", {"u":"t","i":"f","e":"q" }))
# 'mfnfsctlq'

