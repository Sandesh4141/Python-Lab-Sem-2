# 8) Implement a generator called “squares” to yield the square of all numbers from (a) to (b).
# Test it with a “for” loop and print each of the yielded values.
# 
def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = 3
b = 7
print(f"Squares of numbers from {a} to {b}:")
for square in squares(a, b):
    print(square)
