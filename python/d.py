import math

# Given data
sample_proportion = 4781 / 100000
sample_size = 100000
confidence_level = 0.95

# Calculate the critical value (Z-score) for 95% confidence
z_score = 1.96

# Calculate the standard error
standard_error = math.sqrt((sample_proportion * (1 - sample_proportion)) / sample_size)

# Calculate the lower and upper bounds of the confidence interval
lower_bound = sample_proportion - z_score * standard_error
upper_bound = sample_proportion + z_score * standard_error

# Convert the bounds to percentages
lower_bound_percentage = lower_bound * 100
upper_bound_percentage = upper_bound * 100

print(f"A 95% confidence interval for the true proportion of potential donors who may donate is ({lower_bound_percentage:.2f}%, {upper_bound_percentage:.2f}%).")

