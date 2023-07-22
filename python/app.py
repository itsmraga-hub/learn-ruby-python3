import statsmodels.api as sm
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import zt_ind_solve_power

# Given data
n_initial = 70
faulty_cars_initial = 14
margin_of_error = 0.04
confidence_level = 0.90

# Calculate the estimated proportion (p)
p_initial = faulty_cars_initial / n_initial

# Adjust the effect size slightly (increase by 10%)
effect_size_adjusted = proportion_effectsize(p_initial, p_initial + margin_of_error) * 1.10

# Initialize the required sample size and convergence flag
required_sample_size = None
converged = False

# Set the maximum number of iterations to prevent an infinite loop
max_iterations = 1000
iteration = 1

while not converged and iteration <= max_iterations:
    # Calculate the required sample size for the full investigation
    required_sample_size = zt_ind_solve_power(effect_size=effect_size_adjusted,
                                             alpha=1 - confidence_level,
                                             power=1 - (1 - confidence_level) / 2,
                                             alternative='larger')

    # Check if the calculation has converged and the result is valid
    if not (required_sample_size <= 0 or required_sample_size != required_sample_size):
        required_sample_size = int(round(required_sample_size))
        converged = True
    else:
        # Adjust the effect size slightly for the next iteration
        effect_size_adjusted *= 1.10
        iteration += 1

if not converged:
    print("Failed to converge on a solution even after {} iterations.".format(max_iterations))
else:
    print(required_sample_size)

