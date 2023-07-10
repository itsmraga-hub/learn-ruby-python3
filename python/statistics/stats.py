# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression

# # Create a dataframe with the provided data
# data = {
#     'Car': ['Volvo C70 T5', 'Ford Mustang GT', 'BMW Z3 1.9', 'Ford Mustang Premium',
#             'Ford Mustang GT', 'Chevrolet Corvette LT2', 'BMW 2 Series 230i',
#             'Volkswagen Beetle', 'Audi A5 Premium', 'Chevy Corvette', 'Pontiac G6 GT',
#             'Jaguar XJ XJS', 'Mercedes-Benz E-550'],
#     'Age_(yr)': [9, 13, 23, 3, 1, 13, 3, 6, 8, 12, 13, 25, 4],
#     'Price_Advertised_($)': [16900, 9998, 9999, 26499, 36900, 26999, 32354, 16995,
#                               16885, 26500, 5500, 19990, 32598],
#     'Mileage': [75571, 127829, 24773, 16133, 16834, 23523, 19570, 62012, 50998,
#                 24446, 115321, 54485, 39732]
# }

# df = pd.DataFrame(data)

# # Extract the features (Age) and target variable (Price)
# X = df[['Age_(yr)']]
# y = df['Price_Advertised_($)']

# # Perform linear regression
# regression = LinearRegression()
# regression.fit(X, y)

# # Get the coefficients and intercept of the linear model
# slope = regression.coef_[0]
# intercept = regression.intercept_

# # Print the linear model equation
# print(f"Price = {slope:.2f} * Age + {intercept:.2f}")
# print(f"Price = {slope * 13.00 + intercept}")
# print(24500 - 19246)



# print('William')

# Coefficient values
# intercept = -1.263
# slope = 0.00213

# # SAT score
# SAT_score = 2090

# # Predicted GPA
# predicted_GPA = intercept + slope * SAT_score

# print("Predicted GPA:", predicted_GPA)






# import pandas as pd
# import statsmodels.api as sm

# # Create a DataFrame with the given data
# data = {
#     "Car": [
#         "Smart Fortwo Passion", "Volkswagen Beetle", "Volkswagen New Beetle",
#         "Ford Mustang Premium", "Chevrolet Camaro Z28", "Volvo C70 T5",
#         "Pontiac G6 GT", "Chevy Corvette", "BMW 2 Series 230i",
#         "Mini Cooper S", "BMW Z3 1.9", "Chevrolet Corvette LT2",
#         "Audi TT"
#     ],
#     "Age_(yr)": [11, 6, 12, 3, 18, 7, 13, 12, 3, 9, 23, 6, 4],
#     "Price _Advertised_($)": [
#         7995, 16995, 9989, 26499, 29995, 19495, 5500, 26500, 32354,
#         6995, 9999, 48900, 31995
#     ]
# }

# df = pd.DataFrame(data)

# # Add a constant column for the intercept term
# df["Intercept"] = 1

# # Perform the linear regression
# model = sm.OLS(df["Price _Advertised_($)"], df[["Intercept", "Age_(yr)"]])
# results = model.fit()

# # Get the coefficients of the regression equation
# intercept = results.params["Intercept"]
# slope = results.params["Age_(yr)"]

# # Print the regression equation
# print(f"Regression equation: Price = {intercept:.2f} + {slope:.2f} * Age_(yr)")


# print(f"Regression equation: Price = {intercept:.2f} + {slope:.2f} * Age_(yr)")

# price = 30240.6 + -944.2 * 35
# print(price)

# import math

# # Calculate the coefficient of determination (R-squared)
# correlation = 0.907
# r_squared = correlation ** 2

# # Convert R-squared to a fraction
# fraction_variability = r_squared

# # Print the result
# print(f"The fraction of variability in potassium accounted for by fiber content is approximately: {fraction_variability:.2f}")





# import numpy as np

# # Define the data
# sales_people = np.array([2, 4, 7, 8, 10, 10, 12, 15, 15, 20])
# sales = np.array([10, 11, 13, 13, 18, 20, 21, 22, 21, 26])

# # Calculate the correlation coefficient
# correlation_coef = np.corrcoef(sales_people, sales)[0, 1]

# # Print the result
# print("The correlation coefficient for the given data is:", correlation_coef)





# Define the regression model coefficients
# intercept = 47.86
# slope = 0.069

# # Define the size of the house
# size = 2500

# # Calculate the predicted price
# predicted_price = intercept + slope * size

# # Print the result
# print("The predicted price for a 2500-square-foot house is:", predicted_price, "thousand dollars")





# Define the regression model coefficients
intercept = 47.86
slope = 0.069

# Define the size of the house
size = 1100

# Calculate the expected price for a 1100-square-foot house
expected_price = intercept + slope * size

print(expected_price)

# Calculate the asking price by subtracting $5500
asking_price = expected_price - 5500

# Print the result
print("The asking price for a 1100-square-foot house is:", asking_price, "thousand dollars")

