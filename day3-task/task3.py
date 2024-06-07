# Question 3: Chi-Squared Test
# Objective: Perform a Chi-Squared test for independence.
#
# Create a contingency table with observed frequencies for two categorical variables.
#
# |-----------| Category A | Category B |
# | Group 1 |     10        |     20     |
# | Group 2 |     15         |     25       |
#
# Perform a Chi-Squared test to determine if there is a significant association between the two categorical variables.

import numpy as np
from scipy.stats import chi2_contingency

# Create a contingency table with observed frequencies
observed_frequencies = np.array([[10, 20],
                                  [15, 25]])

# Perform a Chi-Squared test
chi2_statistic, p_value, _, _ = chi2_contingency(observed_frequencies)

print("Chi-Squared Test:")
print("Chi-Squared Statistic:", chi2_statistic)
print("P-value:", p_value)
