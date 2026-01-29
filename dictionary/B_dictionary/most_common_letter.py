#Write a function `most_common_letter` that accepts a string as an argument.
#The function should return the character that appears **most frequently** in the string.
#You may assume:
#- There are **no ties**
#- The string contains only lowercase letters

def most_common_letter(str):
    count = {}
    for i in str:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    key = ""
    value = 0
    for k, v in count.items():
        if v > value:
            value = v
            key = k
    return key




print(most_common_letter("building"))
# 'i'

print(most_common_letter("shoestring"))
# 's'

print(most_common_letter("preparedness"))
# 'e'

