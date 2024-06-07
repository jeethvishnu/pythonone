# Question 1: One-Sample t-Test
#
# Perform a one-sample t-test to determine if the sample mean is significantly different from a known population mean.
#
# Generate a sample dataset of 30 random values from a normal distribution with a mean of 60 and a standard deviation of 10.
# Perform a one-sample t-test to check if the sample mean is significantly different from 50.

from scipy.stats import ttest_1samp
import numpy as np

# Generate a sample dataset of 30 random values from a normal distribution with a mean of 60 and a standard deviation of 10
sample_dataset = np.random.normal(60, 10, 30)

# Perform a one-sample t-test to check if the sample mean is significantly different from 50
t_statistic, p_value = ttest_1samp(sample_dataset, 50)

print("One-Sample t-Test:")
print("T-statistic:", t_statistic)
print("P-value:", p_value)
