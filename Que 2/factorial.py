# 3.Write a program to find the factorial of a given 

num = int(input("Enter a number: "))
fact = 1

if num < 0:
    print("Negative number does not exist in factorial")
elif num == 0:
    print("0 factorial is 1")
else:
    for i in range(1, num + 1):
        fact *= i

    print("Factorial of the given number is:", fact)
