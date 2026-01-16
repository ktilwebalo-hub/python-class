
def count_vowels(str):
    counter = 0
    vowels = "aeiou"
    for i in str:
        if i in vowels:
            counter += 1
    return counter

print(count_vowels("hello"))        # 2
print(count_vowels("Programming"))  # 3

