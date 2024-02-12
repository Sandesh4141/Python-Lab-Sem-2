# 5) Write a program to print the sum of natural numbers using recursion.
def sum_of_natural_numbers(n):
    if n == 1:
        return 1  
    else:
        return n + sum_of_natural_numbers(n - 1)  
    # recursive call to sum_of_natutal_numbers function

number = int(input("Enter a positive integer: "))
sum = sum_of_natural_numbers(number)
print("The sum of natural numbers up to", number, "is:", sum)
