# Write a function `total_product(matrix)` that returns the product of all numbers in a 2D list.

def total_product(matrix):
    prod = 1
    sum_prod = 0
    for lists in matrix:  #from the lists, access a list
        for mum in lists: #from the list access each item
            prod *= mum
    return prod

   

array1 = [[3, 5, 2], [6, 2]]
array2 = [[4, 6], [2, 3], [1, 2]]

print(total_product(array1))  # 360
print(total_product(array2))  # 288

