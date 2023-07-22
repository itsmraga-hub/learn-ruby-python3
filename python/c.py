import math

# Given data
margin_of_error = 0.03
sample_size = 1006
estimated_proportion = 0.62

# Calculate Z
z_score = margin_of_error / math.sqrt((estimated_proportion * (1 - estimated_proportion)) / sample_size)

# Convert Z to a confidence level (percentage)
confidence_level = (1 - 2 * (1 - norm.cdf(z_score))) * 100

print("The pollsters used a level of confidence of approximately", round(confidence_level, 2), "%.")

