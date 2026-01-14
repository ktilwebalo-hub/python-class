# Write a function `evens(max_num)` that prints all positive even numbers LESS than max_num.

def evens(max_num):
    even_num = []
    for i in range(max_num):
        if i % 2 == 0:
            even_num.append(i)
    print(even_num)
        

evens(11)
evens(8)

