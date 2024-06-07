# Exercise 4: Implement Broadcasting and Vectorized Operations
#
# a. Broadcasting:
# Create a 3x1 array with values from 1 to 3.
# Create a 1x3 array with values from 4 to 6.
# Add the two arrays using broadcasting.
# Print the resulting array.
#
# b. Vectorized operations:
# Create two large arrays of size 1,000,000 with random values.
# Compute the element-wise product of the two arrays.
# Print the time taken for the computation using vectorized operations.
import time

import numpy as np

# Exercise 4a
arr_3x1 = np.arange(1, 4).reshape(3, 1)
arr_1x3 = np.arange(4, 7).reshape(1, 3)
result_broadcasting = arr_3x1 + arr_1x3
print("\nBroadcasting Result:")
print(result_broadcasting)

# Exercise 4b
large_arr1 = np.random.random(1000000)
large_arr2 = np.random.random(1000000)
start_time = time.time()
result_vectorized = large_arr1 * large_arr2
end_time = time.time()
print("\nTime taken for vectorized operation:", end_time - start_time, "seconds")
