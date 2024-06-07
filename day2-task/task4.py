# Question 4: Descriptive Statistics with NumPy and SciPy
#
# Create a dataset with 20 random values between 1 and 100.
# Compute the following statistics for the dataset:
# Mean
# Median
# Standard deviation
# Variance
# Skewness
# Kurtosis

from scipy.stats import describe
import numpy as np
# Create a dataset with 20 random values between 1 and 100
dataset = np.random.randint(1, 100, 20)

# Compute descriptive statistics for the dataset
stats = describe(dataset)

print("Mean:", stats.mean)
print("Median:", np.median(dataset))
print("Standard deviation:", np.std(dataset))
print("Variance:", np.var(dataset))
print("Skewness:", stats.skewness)
print("Kurtosis:", stats.kurtosis)
