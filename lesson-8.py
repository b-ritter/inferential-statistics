import math
import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt

import pandas as pd

# Study Example

# US families spend an average of $151 on food per week
# in 2012

# μ = 151

# 💰 is the dependent variable

# Treatment is the cost-saving program

# H₀   → μ ≥ 151
# Halt → μ < 151

tcritical = t.ppf(.95, 24)

print(round(tcritical, 3))

# if S = 50
SEM = 50 / math.sqrt(25)

# print(SEM)

d = 126 - 151 # xbar - μ

# t-statistic
tstat = d / SEM

# print(tstat)

# cohen's d
# print(d/50)
# -0.5 👍

tsquared = pow(tstat,2)
# print(tsquared/(tsquared + 24))
# 0.2066115702479339 👍

# x = np.arange(-5,5, .01)
# plt.plot(x, t.pdf(x, 49))
# critical_region = np.arange(-5,-1.711, .01)
# plt.fill_between(critical_region, t.pdf(critical_region, 49), color='lightgray')
# plt.annotate(f't score: {round(t.pdf(tstat,49),2)}', [tstat, t.pdf(tstat, 49)])
# plt.plot(tstat, t.pdf(tstat, 49), marker='o', markersize=5, label='point')
# plt.show()

tcritical_twotailed = t.ppf(.975, 24)
# print(SEM)
MoE = tcritical_twotailed * SEM

# print(MoE)

print(126 - MoE, 126 + MoE)