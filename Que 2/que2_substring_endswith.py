# 2. Write a program to find the words which ends with given character/substring in the inputted string.

input_string = input("Enter String: ")
substring = input("Enter substring: ")
words = input_string.split()

for word in words:
    if word.endswith(substring):
        print(word)
