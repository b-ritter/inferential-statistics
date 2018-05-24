# 3 
# x +/- s/sqrt(n)

#5 

# sdv = 2.8
# compute 95% confidence interval

# we need zscore of sample mean

import math
import numpy as np
from scipy.stats import norm

sample_1 = [8, 9, 12, 13, 14, 16]
mean_sample_1 = np.mean(sample_1)
# s1z = norm.ppf(.95) ❌
# We're looking for 95% total. That leaves
# 2.5% above and below
# s1z = norm.ppf(.90) ❌
s1z = norm.ppf(.975)
# mean_sample_1 +/- Z * 2.8/sqrt(6)
s1lb = mean_sample_1 - s1z * 2.8/math.sqrt(6)
s1ub = mean_sample_1 + s1z * 2.8/math.sqrt(6)
print(f'\
Lower Bound: {s1lb}\n\
Upper Bound: {s1ub}')

# Lower Bound: 9.759574551034188 👌
# Upper Bound: 14.240425448965812 👌


# 6
# σ = 10 <-- represents a percentage
# μ = 68
# 75 +/- Z*10/math.sqrt(25)

Z = norm.ppf(.975) # <-- a .95 confidence interval

me = Z * 10/math.sqrt(25) # <-- margin of error

t = norm(loc=68, scale=2) # <-- use the standard error not the population standard devation

print(1 - t.cdf(75))

print(f'Interval: ({75 - me}, {75 + me}))')

# 12
# σ = 18
# SE = 18/math.sqrt(9) = 6
# μ = 180
# 175 +/- Z*6

# Critical value of Z for a 99% confidence interval
Z = norm.ppf(.995)
# 2.5758293035489004

# Distribution of means?
bp = norm(loc=180, scale=6)

# Percentage of getting 175 or *lower* after treatment
print(bp.cdf(175))

# Margin of error
ME = Z*6

print(175 - ME, 175 + ME)