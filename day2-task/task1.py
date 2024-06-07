# Question 1: Matrix Operations with NumPy
#
# Create two 3x3 matrices A and B with random integer values between 1 and 10.
# Compute the following:
# The sum of A and B.
# The difference between A and B.
# The element-wise product of A and B.
# The matrix product of A and B.
# The transpose of matrix A.
# The determinant of matrix A.

import numpy as np

# Create two 3x3 matrices A and B with random integer values between 1 and 10
A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

# Compute the sum of A and B
sum_result = np.add(A, B)

# Compute the difference between A and B
difference_result = np.subtract(A, B)

# Compute the element-wise product of A and B
elementwise_product_result = np.multiply(A, B)

# Compute the matrix product of A and B
matrix_product_result = np.dot(A, B)

# Compute the transpose of matrix A
transpose_result = np.transpose(A)

# Compute the determinant of matrix A
determinant_result = np.linalg.det(A)

print("Sum of A and B:\n", sum_result)
print("\nDifference between A and B:\n", difference_result)
print("\nElement-wise product of A and B:\n", elementwise_product_result)
print("\nMatrix product of A and B:\n", matrix_product_result)
print("\nTranspose of matrix A:\n", transpose_result)
print("\nDeterminant of matrix A:", determinant_result)
