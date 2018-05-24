import math
import numpy as np
from scipy.stats import norm

# Given a percentage, return a Z-score
Z = norm.ppf(.95)

# print(Z)

Zprime = norm.ppf(.99)

# print(Zprime)

ZZ = norm.ppf(.999)

# print(ZZ)

# 9
# σ = .64
# μ = 7.5
SE = .64/math.sqrt(20)
n = norm(loc=7.5, scale=SE)

z0 = (7.13 - 7.5)/SE

print(z0)


# Two-Tailed Critical Values
# α = .5
print(norm.ppf(.975))

# α = .01
# print(norm.ppf(.995))

# α = .001
# print(norm.ppf(.9995))


import csv
import pandas

df = pandas.read_csv('engagement_2.csv', skiprows=0)

print(df.std(ddof=0)) # N - 1 by default, put in 0 for the population mean
# Please rank how engaged you are in Stats 95 on a scale from 1 to 10.                   2.412989  👍
# Please rank how much you think you're learning in Stats 95 on a scale from 1 to 10.    2.531653
# dtype: float64

SE = 2.41/math.sqrt(50)
print(SE)
# Zscore of 8.3
print((8.3 - 7.47) /SE)

print(1 - norm.cdf(8.3, loc=7.47, scale=0.3408254685319159)) #  👍