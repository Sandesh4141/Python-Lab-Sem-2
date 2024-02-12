# 1.Write a program to find all the indices of a substring in the given string.
def print_index(string, substring):
    flag = False
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            print(i, end=" ")
            flag = True

    if not flag:
        print("no")

string_input = input('Enter a String: ')
substring_input = input('Enter a substring to find: ')
print_index(string_input, substring_input)
