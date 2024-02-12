# 9) Create a generator which will generate the next even number from the number passed. For
# example if the number passed is 3 then the next even number is 4, if the number passed is 6
# then the next even number is 8.

def nextEven(number):
    while True:
        number += 1
        if number % 2 == 0:
            yield number


number = int(input("Enter a number: "))
evenGenerator = nextEven(number)
print("Next even number:", next(evenGenerator))
