# Exercise 2: Perform Basic and Advanced Array Operations
#
# a. Array arithmetic:
# Create two 1-dimensional arrays of integers from 1 to 5 and 6 to 10.
# Perform element-wise addition, subtraction, multiplication, and division and Print the results.
#
# b. Indexing and slicing:
# Create a 5x5 array with values from 1 to 25.
# Extract the subarray consisting of the first two rows and columns.
# Print the extracted subarray.
#
# c. Boolean indexing:
# Create a 1-dimensional array of integers from 10 to 19.
# Extract elements greater than 15.
# Print the resulting array.

import numpy as np

# Exercise 2a
arr1 = np.arange(1, 6)
arr2 = np.arange(6, 11)
print("\nArray 1:", arr1)
print("Array 2:", arr2)
print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)

# Exercise 2b
arr_5x5 = np.arange(1, 26).reshape(5, 5)
subarray = arr_5x5[:2, :2]
print("\nSubarray:")
print(subarray)

# Exercise 2c
arr_1d_10to19 = np.arange(10, 20)
print("\nArray 10 to 19:", arr_1d_10to19)
print("Elements > 15:", arr_1d_10to19[arr_1d_10to19 > 15])
