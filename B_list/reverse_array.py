# Write a function `reverse_array(arr)` that accepts a list as an argument.
# The function should return a list containing the elements of the original list in reverse order.

def reverse_array(list):
    new_list = []
    for i in range(len(list)-1, -1, -1):
        new_list.append(list[i])
    print(new_list)


# Example:
reverse_array(["zero", "one", "two", "three"]) #-> ['three', 'two', 'one', 'zero']
reverse_array([7, 1, 8]) #-> [8, 1, 7]

