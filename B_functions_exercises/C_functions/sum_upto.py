def sum_upto(max_num):
    sum = 0
    for i in range(1, max_num + 1):
        sum += i
    return sum


print(sum_upto(5))   # 15
print(sum_upto(10))  # 55

