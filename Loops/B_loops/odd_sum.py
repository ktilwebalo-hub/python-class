# Write a function `odd_sum(max_num)` that returns the sum of all odd numbers
# from 1 to max_num inclusive.
def odd_sum(max_num):
    sum_odd = 0
    for i in range(1, max_num + 1, 1):
        if i % 2 !=0:
            sum_odd += i
    print(sum_odd)
# Example:
odd_sum(10) #-> 25  # 1 + 3 + 5 + 7 + 9
odd_sum(5)  #-> 9   # 1 + 3 + 5

