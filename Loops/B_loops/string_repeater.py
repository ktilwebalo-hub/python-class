# Write a function `string_repeater(text, n)` that returns a new string
# consisting of `text` repeated `n` times.
def string_repeater(text, n):
    new_string = ""
    for i in range(1, n + 1, 1):
        new_string += text
    
    print(new_string)
# Example:
string_repeater("q", 4)  #-> 'qqqq'
string_repeater("go", 2) #-> 'gogo'
string_repeater("tac", 3) #-> 'tactactac'

