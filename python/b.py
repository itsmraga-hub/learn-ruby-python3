import math

# Given data
initial_sample_size = 40
number_of_faulty_cars = 8
desired_margin_of_error = 0.03
confidence_level = 0.90

# Calculate the estimated proportion
estimated_proportion = number_of_faulty_cars / initial_sample_size

# Calculate the critical value (Z-score) for 90% confidence
z_score = 1.645

# Calculate the required sample size
required_sample_size = (z_score**2 * estimated_proportion * (1 - estimated_proportion)) / (desired_margin_of_error**2)

# Round up to the nearest whole number
required_sample_size = math.ceil(required_sample_size)

print("The environmental agency should sample at least", required_sample_size, "vehicles for the full investigation.")

