# 1) Write the following programs by making use of built-in functions:
# a. To print pyramid of ‘*’.
# b. To sort the words form a string based on their alphabetical order.

#pyramid print

def pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

rows = int(input("Enter the number of Rows: "))
pyramid(rows)

#sort the word from string 
def sort_words(sentence):
    words = sentence.split()
    words.sort()
    return ' '.join(words)

sentence = input("Enter a sentence: ")
sortSent = sort_words(sentence)
print("Sorted Sentence:", sortSent)


