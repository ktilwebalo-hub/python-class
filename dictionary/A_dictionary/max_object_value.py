#Write a function `max_object_value` that accepts a dictionary where:
#keys are strings
#values are numbers
#Return a list containing: 
#the key with the highest value
#the highest value itself

def max_object_value(dict):
    key =  ""
    value = 0
    for k, v in dict.items():
        if v > value:
            value = v
            key = k
    return [key, value]

print(max_object_value({"a":5,"b":2,"c":6,"d":7,"e":4 }))
# ['d', 7]

print(max_object_value({"lychee":11,"rambutan":13,"papaya":9 }))
# ['rambutan', 13]
