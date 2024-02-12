# 9.Write a program to count the number of alphabets, digits and spaces in the given string.

input_str = input("Enter any string: ")
alphas = 0
digits = 0
spaces = 0
other = 0

for ch in input_str:
    if ch.isalpha():
        alphas += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        other += 1

print("There are", alphas, "alphabets")
print("There are", digits, "digits")
print("There are", spaces, "spaces")
print("There are", other, "other characters")
