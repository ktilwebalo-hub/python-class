# Write a function `remove_capitals(text)` that returns a new string with all
# capital letters removed.

def remove_capitals(text):
    str = ' '
    for i in range(len(text)):
        if text[i].lower() == text[i]:
            str = str + text[i]
    print(str)
        
# Example:
remove_capitals("fOrEver")     #-> 'frver'
remove_capitals("raiNCoat")    #-> 'raioat'
remove_capitals("cElLAr Door") #-> 'clr oor'

