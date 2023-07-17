import numpy as np

age = np.array([27.932] * 25)  # Assuming all ages in the sample are 27.932 for demonstration purposes
typ = np.array([577.211] * 25)  # Assuming all Total Yearly Purchases are 577.211 for demonstration purposes

# Calculate the slope and intercept
slope = 0.038 * (240.937 / 8.342)
intercept = 577.211 - slope * 27.932

print(f"The linear regression equation for predicting Total Yearly Purchase from age is: TYP = {intercept:.3f} + {slope:.3f} * age")
print(f"{intercept + (slope * 50)}")
