# Question 2: Two-Sample t-Test
# Perform a two-sample t-test to compare the means of two independent samples.
#
# Generate two sample datasets each with 25 random values from normal distributions with means of 55 and 60, and a standard deviation of 8.
# Perform an independent two-sample t-test to check if the means of the two samples are significantly different.


import numpy as np
from scipy.stats import ttest_ind

# Generate two sample datasets
sample_dataset1 = np.random.normal(55, 8, 25)
sample_dataset2 = np.random.normal(60, 8, 25)

# Perform an independent two-sample t-test to check if the means of the two samples are significantly different
t_statistic, p_value = ttest_ind(sample_dataset1, sample_dataset2)

print("Two-Sample t-Test:")
print("T-statistic:", t_statistic)
print("P-value:", p_value)
