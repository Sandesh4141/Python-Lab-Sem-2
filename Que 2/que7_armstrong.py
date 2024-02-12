# 7. Program to find Armstrong number(s) in an interval

num = int(input('Enter a number '))
newnum = temp = num
count = 0
add = 0
num1 = 0
digit_sum = 0
sum = 0

while num > 0:
    num1 = num % 10
    num = num // 10
    print(num1)
    count = count + 1

print('The digit Length is ', count)

while newnum != 0:
    num1 = newnum % 10
    newnum = newnum // 10
    sum = num1 ** count
    add = add + sum

if add == temp:
    print('Given is Armstrong')
else:
    print('Given Number is Not Armstrong')
