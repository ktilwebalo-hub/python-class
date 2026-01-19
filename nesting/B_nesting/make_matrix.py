# Write a function `make_matrix(m, n, value)` that returns a 2D list of m rows and n columns
# filled with `value`.

def make_matrix(m, n, value):
    new_list = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(value)
        new_list.append(row)
    return new_list
    

print(make_matrix(3, 5, None))
print(make_matrix(4, 2, "x"))
print(make_matrix(2, 2, 0))

# Example [
#[None, None, None, None, None],
#[None, None, None, None, None],
#[None, None, None, None, None]
 #]