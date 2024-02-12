# 5.Write a program to find GCD of two numbers

m = int(input("Enter first positive number: "))
n = int(input("Enter second positive number: "))

if m == 0 and n == 0:
    print("Invalid input")
if m == 0:
    print(f"GCD is {n}")
if n == 0:
    print(f"GCD is {m}")

while m != n:
    if m > n:
        m = m - n
    elif n > m:
        n = n - m

print(f"GCD of two numbers is {m}")
