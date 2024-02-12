# Question:
# Write a program to do summation of diagonal elements of a matrix.

def diagonal_sum(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        print("Invalid matrix. Please provide a square matrix.")
        return None

    diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
    return diagonal_sum


def get_matrix_from_user():
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))

        matrix = []

        print("Enter the matrix elements row-wise:")
        for i in range(rows):
            row = list(map(int, input().split()))
            if len(row) != cols:
                print(f"Row {i+1} should have {cols} elements. Please try again.")
                return None

            matrix.append(row)

        return matrix

    except ValueError:
        print("Invalid input. Please enter numeric values for matrix elements.")
        return None


# Get matrix from user
user_matrix = get_matrix_from_user()

if user_matrix is not None:
    result = diagonal_sum(user_matrix)

    if result is not None:
        print("\nMatrix:")
        for row in user_matrix:
            print(row)

        print("\nSum of Diagonal Elements:", result)
