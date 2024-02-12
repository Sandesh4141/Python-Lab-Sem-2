# 2) Write a user defined function
# a. average() which will return the average of the numbers inputted by the user.
# b. nMax() which will return the maximum between the entered numbers.

def average(numb):
    # taking array as input
    total = 0
    count = 0
    for num in numb:
        total += num
        count += 1
    return total / count

result = average([455, 66])
print("The average is:", result)

# maximum number return
def nMax(*args):
    if not args:
        return print("Enter valid arguments")  
    max_num = args[0]  # Initialize max_num = first argument
    for num in args[1:]:  # Iterate
        if num > max_num:  # Compare num === current max_num
            max_num = num  # Update max_num if num > greater
    return max_num


result = nMax(10, 5, 20, 15, 30)
print("Max Number :", result)
