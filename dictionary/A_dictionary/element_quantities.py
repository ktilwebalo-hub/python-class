#Write a function `element_quantities` that accepts a dictionary where:
#- keys are elements
# values are quantities
#Return a list containing each element repeated according to its quantity.

def element_quantities(dict):
    new_list = []

    for keys, values in dict.items():
        for i in range(values):
            new_list.append(keys)
    return new_list
        



quantities1 = {"cat":3,"bird":1,"dog":2 }
print(element_quantities(quantities1))
# ['cat', 'cat', 'cat', 'bird', 'dog', 'dog']

quantities2 = {"blue":3,"brown":1 }
print(element_quantities(quantities2))
# ['blue', 'blue', 'blue', 'brown']

