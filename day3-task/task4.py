# Question 4: One-Way ANOVA
# Objective: Perform a one-way ANOVA to compare means across multiple groups.
#
# Generate three sample datasets each with 20 random values from normal distributions with means of 50, 55, and 60, and a standard deviation of 10.
# Perform a one-way ANOVA to check if there are any significant differences in means across the three groups.

import numpy as np
from scipy.stats import f_oneway

# Generate three sample datasets
sample_dataset1 = np.random.normal(50, 10, 20)
sample_dataset2 = np.random.normal(55, 10, 20)
sample_dataset3 = np.random.normal(60, 10, 20)

# Perform a one-way ANOVA
f_statistic, p_value = f_oneway(sample_dataset1, sample_dataset2, sample_dataset3)

print("One-Way ANOVA:")
print("F-statistic:", f_statistic)
print("P-value:", p_value)
