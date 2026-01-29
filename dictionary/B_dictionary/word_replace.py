#Write a function `word_replace` that accepts:

#- a sentence string
#- a dictionary

#The function should return a new sentence where words that appear 
#as keys in the dictionary are replaced with their corresponding valuesprint(word_replace(
#"I never take naps during the day",
#   {"never":"always","day":"weekend" }
#))
# 'I always take naps during the weekend'

def word_replace(senten, dict):
    list_ = senten.split(" ")
    new_list = []
    for word in list_:
        if word in dict:
            new_list.append(dict[word])
        else:
            new_list.append(word)
    return " ".join(new_list)


        




print(word_replace(
"the park is closed",
    {"closed":"open","the":"a" }
))
# 'a park is open'

print(word_replace(
"I do what I want",
    {"I":"we","cat":"dog" }
))
# 'we do what we want'

