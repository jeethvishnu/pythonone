# Question 5: Post-hoc Test using Tukey's HSD
# Objective: Perform a post-hoc test using Tukey's HSD to identify which groups are significantly different.
#
# Use the same datasets generated in the one-way ANOVA exercise.
# Perform Tukey's HSD test to find out which pairs of group means are significantly different.

import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Generate three sample datasets
sample_dataset1 = np.random.normal(50, 10, 20)
sample_dataset2 = np.random.normal(55, 10, 20)
sample_dataset3 = np.random.normal(60, 10, 20)


# Combine all datasets into one
combined_data = np.concatenate([sample_dataset1, sample_dataset2, sample_dataset3])

# Create corresponding group labels
group_labels = ['Group 1'] * 20 + ['Group 2'] * 20 + ['Group 3'] * 20

# Perform Tukey's HSD test
tukey_results = pairwise_tukeyhsd(combined_data, group_labels)

print("Tukey's HSD Test:")
print(tukey_results)
