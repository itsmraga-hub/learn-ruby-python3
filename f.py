import scipy.stats as stats

# Given data
sample_proportion = 0.453
sample_size = 1058
confidence_level = 0.90

# Calculate the margin of error with 90% confidence level
critical_value = stats.norm.ppf(1 - (1 - confidence_level) / 2)
margin_of_error = critical_value * ((sample_proportion * (1 - sample_proportion)) / sample_size) ** 0.5

# Print the result
print(margin_of_error)

