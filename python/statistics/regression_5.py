# # Given information
# r = -0.6243
# mean_HCI = 342.27
# std_HCI = 119.071
# mean_MFI = 46210.10
# std_MFI = 7003.548

# # Calculate the slope (β1)
# beta1 = r * (std_HCI / std_MFI)

# # Calculate the intercept (β0)
# beta0 = mean_HCI - beta1 * mean_MFI

# # Print the equation of the regression line
# print("HCI = {:.2f} + {:.2f} * MFI".format(beta0, beta1))


# Given equation coefficients
beta0 = -148.2064
beta1 = 0.0106

# Given MFI value
MFI = 44993

# Calculate the predicted HCI
HCI = beta0 + beta1 * MFI

# # Print the predicted HCI
# print("Predicted HCI:", HCI)

# print(548.02 - HCI)



# Given mean and standard deviation values
mean_HCI = 342.27
std_HCI = 119.071
mean_MFI = 46210.10
std_MFI = 7003.548
correlation_coefficient = -0.6243

# Standardize the variables
Zhci = (HCI - mean_HCI) / std_HCI
Zmfi = (MFI - mean_MFI) / std_MFI

# Calculate the coefficient beta1
beta1 = correlation_coefficient * (std_HCI / std_MFI)

# Print the standardized regression equation
print("Zhci = {} + {} * Zmfi".format(beta0, beta1))
