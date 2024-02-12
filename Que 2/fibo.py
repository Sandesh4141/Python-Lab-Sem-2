# 4.Write a program to display Fibonacci sequence up to n-th term

num = int(input("Enter Number: "))
x, y = 0, 1
c = 2

print("Fibonacci sequence is:")
print(x)
print(y)

while c < num:
    z = x + y
    print(z)
    x, y = y, z
    c += 1
