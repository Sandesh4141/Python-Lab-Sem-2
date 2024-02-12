# 6.Write a program to print all prime numbers in an interval.

start = 10
stop = 50

for num in range(start, stop + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print("Prime number is:", num)
