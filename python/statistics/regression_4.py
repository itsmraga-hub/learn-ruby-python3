import pandas as pd
import statsmodels.api as sm

# Create a DataFrame with the Waist and % Body Fat data
data = {
    'Waist': [32, 35, 38, 32, 39, 40, 40, 34, 39, 37, 33, 40, 35, 32, 45, 32, 42, 34, 35, 43],
    'BodyFat': [6, 21, 16, 6, 21, 32, 31, 21, 25, 32, 11, 19, 23, 9, 37, 10, 26, 13, 10, 28]
}
df = pd.DataFrame(data)

# Add a constant column for the intercept term
df['intercept'] = 1

# Fit the linear regression model
model = sm.OLS(df['BodyFat'], df[['intercept', 'Waist']])
results = model.fit()

# Get the R-squared value
r_squared = results.rsquared
print("R-squared value:", r_squared)

# Get the standard error
se = results.bse['Waist']
print("Standard error (Se):", se)