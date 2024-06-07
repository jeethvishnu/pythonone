# Question 5: Hypothesis Testing with SciPy
# Generate a sample dataset of 30 random values from a normal distribution with mean 50 and standard deviation 5.
# Perform a one-sample t-test to check if the sample mean is significantly different from 50."

import numpy as np

from scipy.stats import ttest_1samp

# Generate a sample dataset of 30 random values from a normal distribution with mean 50 and standard deviation 5
sample_dataset = np.random.normal(50, 5, 30)

# Perform a one-sample t-test to check if the sample mean is significantly different from 50
t_statistic, p_value = ttest_1samp(sample_dataset, 50)

print("T-statistic:", t_statistic)
print("P-value:", p_value)
