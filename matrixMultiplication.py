# Creation of variables for matrix dimensions
rows_matrix1 = 0
columns_matrix1 = 0
rows_matrix2 = 0
columns_matrix2 = 0

# Ask the user for the dimensions of the matrices to be multiplied
print("Select the number of rows for the first matrix: ")
rows_matrix1 = int(input())
print("Select the number of columns for the first matrix: ")
columns_matrix1 = int(input())

print("Select the number of rows for the second matrix: ")
rows_matrix2 = int(input())
print("Select the number of columns for the second matrix: ")
columns_matrix2 = int(input())

# Creation of matrices
first_matrix = [[0 for _ in range(columns_matrix1)] for _ in range(rows_matrix1)]

second_matrix = [[0 for _ in range(columns_matrix2)] for _ in range(rows_matrix2)]

# Input values for the matrices
print("Enter values for the first matrix:")
for i in range(rows_matrix1):
    for j in range(columns_matrix1):
        first_matrix[i][j] = int(input(f"Enter the value for position ({i+1}, {j+1}): "))
print("")

print("Enter values for the second matrix:")
for i in range(rows_matrix2):
    for j in range(columns_matrix2):
        second_matrix[i][j] = int(input(f"Enter the value for position ({i+1}, {j+1}): "))

print("")
# Display the matrices to be multiplied
print("First matrix: ")
print(first_matrix)
print("Second matrix: ")
print(second_matrix)

# Check if multiplication is possible and perform the operation if so
if columns_matrix1 == rows_matrix2:
    print("")
    # Initialize a resulting matrix with zeros
    result = [[0 for _ in range(columns_matrix2)] for _ in range(rows_matrix1)]
    for i in range(rows_matrix1):
        for j in range(columns_matrix2):
            for k in range(rows_matrix2):
                result[i][j] += first_matrix[i][k] * second_matrix[k][j]
    print("The result of the multiplication is: ")
    print(result)
else:
    print("The operation cannot be performed as the number of columns in the first matrix is not equal to the number of rows in the second matrix")
    exit()
