# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def read_matrix(rows, cols, name):
    print("Enter " + name + ":")
    matrix = []
    for i in range(rows):
        row_input = input("Enter row " + str(i + 1) + ": ")
        row = row_input.split()
        row = [int(x) for x in row]
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    for row in matrix:
        line = ""
        for value in row:
            line = line + str(value) + " "
        print(line)

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result

def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)
    return result

def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total = total + matrix_a[i][k] * matrix_b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result

print("PART A - Transpose a Matrix")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = read_matrix(rows, cols, "matrix")
print("Original Matrix:")
display_matrix(matrix)
print("Transposed Matrix:")
transposed = transpose_matrix(matrix)
display_matrix(transposed)

print()
print("PART B - Add Two Matrices")
rows_b = int(input("Enter number of rows: "))
cols_b = int(input("Enter number of columns: "))
matrix_a = read_matrix(rows_b, cols_b, "matrix A")
matrix_b = read_matrix(rows_b, cols_b, "matrix B")
sum_result = add_matrices(matrix_a, matrix_b)
print("Sum Matrix:")
display_matrix(sum_result)

print()
print("PART C - Multiply Two Matrices")
rows_c = int(input("Enter rows for matrix A: "))
cols_c = int(input("Enter columns for matrix A (rows for matrix B): "))
cols_p = int(input("Enter columns for matrix B: "))
matrix_c1 = read_matrix(rows_c, cols_c, "matrix A")
matrix_c2 = read_matrix(cols_c, cols_p, "matrix B")
product_result = multiply_matrices(matrix_c1, matrix_c2)
print("Product Matrix:")
display_matrix(product_result)
