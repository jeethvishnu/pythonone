# Exercise 3: Use NumPy for Mathematical and Statistical Calculations
#
# a. Mathematical functions:
# Create an array of 10 evenly spaced values between 0 and 2π.
# Compute the sine, cosine, and tangent of each value.
# Print the results.
#
# b. Statistical functions:
# Create a 3x3 array with random integers between 1 and 100.
# Compute the mean, median, standard deviation, and variance.
# Print the results.

import numpy as np

# Exercise 3a
evenly_spaced_values = np.linspace(0, 2 * np.pi, 10)
print("\nEvenly Spaced Values:", evenly_spaced_values)
print("Sine:", np.sin(evenly_spaced_values))
print("Cosine:", np.cos(evenly_spaced_values))
print("Tangent:", np.tan(evenly_spaced_values))

# Exercise 3b
random_array = np.random.randint(1, 101, size=(3, 3))
print("\nRandom Array:")
print(random_array)
print("Mean:", np.mean(random_array))
print("Median:", np.median(random_array))
print("Standard Deviation:", np.std(random_array))
print("Variance:", np.var(random_array))

