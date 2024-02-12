#3) Write a program to find the factorial of a number using recursion.


def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number: "))
if number < 0:
    print("Number is less than 0.")
else:
    print("Factorial of", number, "is", factorial(number))
