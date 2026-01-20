# Write a function `remove_dupes(lst)` that accepts a list and returns a new list
# where each element appears only once.

def remove_dupes(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)

    return new_list
# Example usage:
print(remove_dupes(["x", "y", "y", "x", "z"]))  # ['x', 'y', 'z']
print(remove_dupes([False, False, True, False]))  # [False, True]
print(remove_dupes([42, 5, 7, 42, 7, 3, 7, 7]))  # [42, 5, 7, 3]

