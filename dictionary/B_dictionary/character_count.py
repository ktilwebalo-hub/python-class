#Write a function `character_count` that accepts a string as an argument.

#The function should return a **dictionary** containing the count of each character in the string.

def character_count(str):
    result = {}
    for ch in str:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    return result



print(character_count("evening"))
# { 'e': 2, 'v': 1, 'n': 2, 'i': 1, 'g': 1 }

print(character_count("mississippi"))
# { 'm': 1, 'i': 4, 's': 4, 'p': 2 }

print(character_count("chili"))
# { 'c': 1, 'h': 1, 'i': 2, 'l': 1 }

