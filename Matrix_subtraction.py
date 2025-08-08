# Matrix Subtraction Program

# Function to subtract two matrices
def subtract_matrices(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] - mat2[i][j])
        result.append(row)
    return result

# Example matrices
matrix1 = [
    [5, 8, 7],
    [6, 4, 3],
    [2, 9, 1]
]

matrix2 = [
    [1, 2, 3],
    [3, 1, 2],
    [5, 4, 3]
]

# Subtract
result = subtract_matrices(matrix1, matrix2)

# Print result
print("Matrix Subtraction Result:")
for row in result:
    print(row)
