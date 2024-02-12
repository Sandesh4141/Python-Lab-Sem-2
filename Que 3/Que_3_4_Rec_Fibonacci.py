# 4) Write a program to generate a fibonacci sequence using recursion.

def fibonacci(n):
    if n <= 1:  
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) 

def fibo_sequence(num_terms):
    fibonacci_sequence = []
    for i in range(num_terms):
        fibonacci_sequence.append(fibonacci(i))
    return fibonacci_sequence

num_terms = int(input("Enter the number of terms in Fibonacci sequence: "))
if num_terms <= 0:
    print("Number of terms should be a positive integer.")
else:
    fibonacci_sequence = fibo_sequence(num_terms)
    print("Fibonacci sequence:", fibonacci_sequence)
