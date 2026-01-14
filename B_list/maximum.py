# Write a function `maximum(numbers)` that accepts a list of numbers.
# The function should return the largest number in the list.
# If the list is empty, return None.

def maximum(numbers):
    if len(numbers) == 0:
        return None
    
    large_n = 0
    for i in numbers:
        if i > large_n:
            large_n = i
    print(large_n)
# Example:
maximum([5, 6, 3, 7]) #-> 7
maximum([17, 15, 19, 11, 2]) #-> 19
maximum([]) #-> None

