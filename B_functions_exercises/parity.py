# Write a function `parity` that accepts a number.
# Return the string "even" if the number is even.
# Return the string "odd" if the number is odd.

def parity(num):
    if num % 2 == 0:
        print("Even")

    else:
        print("Odd")

num_ = int(input("Input a number of your choice: "))
parity(num_)