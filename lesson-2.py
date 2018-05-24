# Lesson 10
# Confidence interval
# 2.71 is the standard error
# 1.96 is the z-score that represents
# print(40 + 1.96*2.71)
# print(40 - 1.96*2.71)

# print(40 + 1.96*1.01)
# print(40 - 1.96*1.01)

import math
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Question 16

# Given a percentage, returns a z-score
zscore_1 = norm.ppf(.99)
zscore_1 = round(zscore_1, 2)
# 2.3263478740408408 SE's away from mean
print(zscore_1)

# 17
print(40 + 1.01*zscore_1)
print(40 - 1.01*zscore_1) 

# 19

import csv
with open('engagement.csv') as f:
  data = csv.reader(f)
  dataset = [float(item.pop()) for item in data]

def rt3(x):
  return round(x, 3)

standard_dev = np.std(dataset)
mean = np.mean(dataset)

print(f'\
Standard Deviation: {rt3(standard_dev)} \n\
Mean:               {rt3(mean)}\
')

# Standard Deviation: 0.107 👍
# Mean:               0.077 👍

# 22
# SE = σ/math.sqrt(N) = 0.107/sqrt(20) = 0.024 👍
print(round(0.107/math.sqrt(20),3)) 

# 23
# .13 +/- 2 * .024
# μI +/- 2 * SE <-- 
print(.13 - 2*.024)
print(.13 + 2*.024)

# 29
# σ_e = .64
# σ_l = .73
print(.64/math.sqrt(20)) 
print(.73/math.sqrt(20))
# 0.14310835055998652 👍
# 0.16323296235748463 👍

# 30
print((8.94-7.5)/0.14310835055998652)
# 10.06230589874905
print((8.35-8.2)/0.16323296235748463 )
# 0.918932045547861

engagement = norm(loc=7.5, scale=0.14310835055998652)

learning = norm(loc=8.2, scale=0.16323296235748463)

print(1 - engagement.cdf(8.94))

# Input the actual score into CDF
# to yield the percentage
print(1 - learning.cdf(8.35))

