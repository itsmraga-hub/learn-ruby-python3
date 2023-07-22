import statsmodels.stats.api as sms

# Given data
sample_proportion = 0.2    # Estimated proportion of cars with faulty emissions systems (20%)
margin_of_error = 0.04     # Desired margin of error (4%)
confidence_level = 0.9     # Desired confidence level (90%)

# Calculate the effect size (minimum detectable effect size)
effect_size = sms.proportion_effectsize(sample_proportion, sample_proportion + margin_of_error)

# Calculate the required sample size
required_sample_size = sms.NormalIndPower().solve_power(effect_size=effect_size, alpha=1-confidence_level, power=confidence_level, alternative='two-sided')

# Round up to the nearest whole number
required_sample_size = round(required_sample_size)

print("The environmental agency should sample at least", required_sample_size, "vehicles for the full investigation.")

