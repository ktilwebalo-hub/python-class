# Write a function `zipper(list1, list2)` that returns a 2D list containing pairs of elements at
# the same indices. Assume lists have same length.

def zipper(list1, list2):
    new_list = []
    for i in range(len(list1)):
        row = []
        for j in range(len(list2)):
            if i == j:
                row.append([list1[i], list2[j]])

        new_list.append(row)
    return new_list
    
array1 = ["a", "b", "c", "d"]
array2 = [-1, -2, -3, -4]
print(zipper(array1, array2))

array3 = ["whisper", "talk", "shout"]
array4 = ["quiet", "normal", "loud"]
print(zipper(array3, array4))
