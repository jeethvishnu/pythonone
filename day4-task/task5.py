# Exercise 5: Optimize Performance Using Vectorization and Numba
#
# a. Vectorization:
# Create a function to compute the element-wise square of an array using a for loop.
# Create another function to perform the same computation using NumPy vectorization.
# Compare the performance of the two functions using a large array of size 1,000,000.
#
# b. Numba:
# Use the @numba.jit decorator to optimize the function from step 1 that uses a for loop.

# Compare the performance of the Numba-optimized function with the vectorized NumPy function.


import time
# import numba

import numpy as np

# Exercise 5a
def square_with_loop(arr):
    result = np.empty_like(arr)
    for i in range(len(arr)):
        result[i] = arr[i] ** 2
    return result

large_array = np.random.random(1000000)

start_time = time.time()
result_loop = square_with_loop(large_array)
end_time = time.time()
print("\nTime taken for loop computation:", end_time - start_time, "seconds")

start_time = time.time()
result_vectorized = large_array ** 2
end_time = time.time()
print("Time taken for vectorized computation:", end_time - start_time, "seconds")

# Exercise 5b
# @numba.jit
def square_with_numba(arr):
    result = np.empty_like(arr)
    for i in range(len(arr)):
        result[i] = arr[i] ** 2
    return result

start_time = time.time()
result_numba = square_with_numba(large_array)
end_time = time.time()
print("Time taken for Numba-optimized computation:", end_time - start_time, "seconds")
