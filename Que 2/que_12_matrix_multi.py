# Question:
# Write a program to perform matrix multiplication.

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[5,6,9],
     [6,7,0],
     [4,5,9]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print("Multiplication of two matrices is:")
for r in result:
    print(r)
