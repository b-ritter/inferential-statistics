import math
import numpy as np
from scipy.stats import norm


# 2
# σ = 6
# μ = 25
# α = .05
# N = 36

# SE = 6/6 = 1
# Zscore = 28 - 25 / 1 = 3

music = norm(loc=25, scale=6)

# print(1 - music.cdf(28))

# Returns correct Z-Critical value for α = .05
# print(norm.ppf(.95))

# 11
# σ = .36
# μ = 22.965
# α = .05
# N = 16

# SE = .36/math.sqrt(16) = .36/4 = .09

z_sprinting = (22.793 - 22.965) / .09

# print(z_sprinting)


# 13
# σ = 230
# μ = 7895
# α = .05
# N = 5

SE = 230 / math.sqrt(5)
z_flowers = (9640 - 7895) / SE

print(z_flowers)
