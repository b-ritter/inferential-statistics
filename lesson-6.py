import math
import numpy as np
from scipy.stats import t

import pandas as pd

# print(t.ppf(.95, df=12))

# Sample size of 30
# Degrees of freedom are N-1
# print(t.ppf(.975, df=29))

# Given a t-statistic, returns the probability of 
# getting a result greater
# You could also call this the survival function
# print(1 - t.cdf(2.45, df=23))

df = pd.read_csv('Finches - Lesson 10 - Sheet1.csv', skiprows=0)

# print(df.describe())

d = 6.47 - 6.07
SE = .4/math.sqrt(500)
# print(d/SE)

# μ = 10
# α = .05

sample = pd.Series([5, 19, 11, 23, 12, 7, 3, 21])

s_delta = sample.mean() - 10
s_SE = sample.std() / math.sqrt(sample.size) # n-1 is incorrect

print(s_delta/s_SE)
# 0.977461894333816

# Two-tailed p-value is equal to:
one_tail = 1 - t.cdf(0.977461894333816, df=7)
print(2*one_tail)


# μ = 1830
# α = .05
# n = 25
# M = 1700
# S = 200

# t-Critical values are 2.064 and -2.064
# Can also be calculated with
# We give the probability and degrees of freedom as input
rent_t_critical = t.ppf(.975, df=24)

rent_d = 1700 - 1830
rent_se = 200/math.sqrt(25)
rent_t_stat = rent_d/rent_se
print("t-stat:" + str(rent_t_stat))

# Cohen's d
print("Cohen's d:" + str((1700 - 1830)/200))

# Confidence Interval
import operator

def ci(op, val, q):
  return round(op(val, q),2)
print([ci(op, 1700, rent_t_critical * rent_se) for op in [operator.sub, operator.add]])
# math.round((rent_t_critical * rent_se)