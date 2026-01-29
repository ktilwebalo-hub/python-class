#Write a function `key_pair` that accepts:
#two dictionaries
# a key string
def key_pair(dict1, dict2, key_):
    return [dict1[key_], dict2[key_]]

cat1 = {"name":"jinkee","breed":"calico" }
cat2 = {"name":"garfield","breed":"red tabby" }

print(key_pair(cat1, cat2,"breed"))
# ['calico', 'red tabby']

print(key_pair(cat1, cat2,"name"))
# ['jinkee', 'garfield']

