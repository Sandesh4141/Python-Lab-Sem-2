# 10. Write a program to convert the last character of each word in the string to uppercase.
# For example:
# Input: "Python programming is very easy to learn"
# Output: "PythoN programminG iS verY easY tO learN"

s = input("Enter a string: ")
print("String before:", s)

words = s.split()
res = []

for word in words:
    if word[-1].isalpha():
        word = word[:-1] + word[-1].upper()
    res.append(word)

res = " ".join(res)
print("String after:", res)
