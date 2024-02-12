# 13.Write a program to transpose the matrix
row = int(input('Enter number of rows: '))
col = int(input('Enter number of columns: '))

# Input matrix
matrix = [[int(input(f'Enter element at row {i+1}, column {j+1}: ')) for j in range(col)] for i in range(row)]

# Transpose matrix
transpose = [[0 for i in range(row)] for j in range(col)]

print("\nMatrix:")
for i in matrix:
    print(i)

for i in range(row):
    for j in range(col):
        transpose[j][i] = matrix[i][j]

print("\nTranspose of matrix:")
for i in transpose:
    print(i)
