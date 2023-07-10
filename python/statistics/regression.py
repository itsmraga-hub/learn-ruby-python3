import statsmodels.api as sm
import numpy as np

# Input the data
X = np.array([2, 3, 7, 8, 10, 10, 11, 14, 17, 19])
Y = np.array([10, 11, 13, 14, 19, 20, 20, 23, 23, 27])

# Add a constant term to the X variable
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(Y, X)
results = model.fit()

# Print the regression equation
intercept = results.params[0]
slope = results.params[1]
print(f"Regression Equation: Y = {intercept:.3f} + {slope:.3f}X")
