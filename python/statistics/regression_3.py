import numpy as np
from sklearn.linear_model import LinearRegression

# Waist size (in inches)
waist = np.array([32, 35, 38, 32, 39, 40, 40, 34, 39, 37, 33, 40, 35, 32, 45, 32, 42, 34, 35, 43])

# Weight (in pounds)
weight = np.array([176, 180, 200, 158, 197, 191, 206, 173, 187, 189, 189, 241, 174, 169, 245, 160, 216, 159, 145, 219])

# Body Fat Percentage
body_fat = np.array([6, 21, 16, 6, 21, 32, 31, 21, 25, 32, 11, 19, 23, 9, 37, 10, 26, 13, 10, 28])

# Perform linear regression
regression_model = LinearRegression()
regression_model.fit(waist.reshape(-1, 1), body_fat)

# Get the regression coefficients
intercept = regression_model.intercept_
slope = regression_model.coef_[0]

# Print the equation of the regression line
print(f"Regression line equation: Body Fat (%) = {intercept:.2f} + {slope:.2f} * Waist (in.)")
