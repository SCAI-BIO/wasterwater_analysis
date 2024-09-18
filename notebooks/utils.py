import math
from scipy.stats import norm
from scipy import stats
import numpy as np

def correlation_confidence_interval(r, n, confidence_level=0.95):
    # Fisher transformation
    if r == 1.0:
        print("Calculation only possible for values less than 1")
    else:    
        z = 0.5 * math.log((1 + r) / (1 - r))

        # Standard error
        SE_z = 1 / math.sqrt(n - 3)

        # Z critical value for the confidence level
        z_alpha_half = norm.ppf(1 - (1 - confidence_level) / 2)

        # Confidence interval in z space
        z_lower = z - z_alpha_half * SE_z
        z_upper = z + z_alpha_half * SE_z

        # Inverse Fisher transformation to get back to correlation scale
        r_lower = (math.exp(2 * z_lower) - 1) / (math.exp(2 * z_lower) + 1)
        r_upper = (math.exp(2 * z_upper) - 1) / (math.exp(2 * z_upper) + 1)

        return r_lower, r_upper

# Example usage
#r = 0.6322508448491246  # correlation coefficient
#n = 84   # sample size 84 for weekly data and 582 for daily data (depends on length of not na df)
#confidence_level = 0.95
#ci_lower, ci_upper = correlation_confidence_interval(r, n, confidence_level)
#print(f"Confidence interval: ({ci_lower:.4f}, {ci_upper:.4f})")


def calculate_CI(metric_list):
    # Calculate sample mean and standard error
    data = metric_list
    mean = np.mean(data)
    sem = stats.sem(data)  # Standard error of the mean
    
    # Calculate the confidence interval
    confidence_level = 0.95
    confidence_interval = stats.t.interval(confidence_level, len(data)-1, loc=mean, scale=sem)
    confidence_interval = [f"{num:.2f}" for num in confidence_interval]
    return confidence_interval