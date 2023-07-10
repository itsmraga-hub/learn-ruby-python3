import numpy as np
from sklearn.linear_model import LinearRegression

# Input the data
X = np.array([2, 3, 7, 8, 10, 10, 11, 14, 17, 19])
Y = np.array([10, 11, 13, 14, 19, 20, 20, 23, 23, 27])

# Reshape the X array to fit the sklearn LinearRegression model
X = X.reshape(-1, 1)

# Create a linear regression model
regression_model = LinearRegression()

# Fit the model to the data
regression_model.fit(X, Y)

# Calculate the R-squared value
r_squared = regression_model.score(X, Y)

# Print the R-squared value
print("R-squared value:", r_squared)
