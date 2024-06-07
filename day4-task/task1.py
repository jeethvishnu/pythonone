# Exercise 1: Create different types of NumPy arrays and perform basic manipulations.
#
# a. Create a 1-dimensional array:
# Create a 1-dimensional array of integers from 0 to 9.
# Print the array and its shape.
#
# b. Create a 2-dimensional array:
# Create a 2-dimensional array (3x3) with values from 1 to 9.
# Print the array, its shape, and the sum of all elements.
#
# c. Reshape the array:
# Reshape the 1-dimensional array from step 1 into a 2x5 array.
# Print the reshaped array and its shape.



import numpy as np

# Exercise 1a
arr_1d = np.arange(10)
print("1D Array:")
print(arr_1d)
print("Shape:", arr_1d.shape)

# Exercise 1b
arr_2d = np.arange(1, 10).reshape(3, 3)
print("\n2D Array:")
print(arr_2d)
print("Shape:", arr_2d.shape)
print("Sum of all elements:", np.sum(arr_2d))

# Exercise 1c
reshaped_arr = arr_1d.reshape(2, 5)
print("\nReshaped Array:")
print(reshaped_arr)
print("Shape:", reshaped_arr.shape)
