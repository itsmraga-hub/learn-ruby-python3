import numpy as np
import statsmodels.api as sm

# Fat variable
fat = np.array([21, 32, 35, 36, 40, 39, 41])

# Calories variable
calories = np.array([400, 570, 610, 560, 630, 680, 670])

# Calculate the correlation coefficient
# correlation_coefficient = np.corrcoef(fat, calories)[0, 1]

# Print the correlation coefficient
# print(f"Correlation coefficient: {correlation_coefficient:.1f}")

fat = sm.add_constant(fat)

# Fit the regression model
model = sm.OLS(calories, fat)
results = model.fit()

# Print the regression equation
intercept = results.params[0]
slope = results.params[1]
print(f"Regression Equation: Y = {intercept:.3f} + {slope:.3f}X")




# Regression equation coefficients
intercept = 129.091
slope = 13.182

# Fat content of the new burger
fat = 26

# Calculate the predicted value (calories)
predicted_calories = intercept + slope * fat

# Given residual
residual = 14

# Calculate the actual value (calories)
actual_calories = predicted_calories + residual

# Print the number of calories for the burger
print(f"The burger with 26 grams of fat has approximately {actual_calories:.2f} calories.")
