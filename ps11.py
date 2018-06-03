import math

import pandas as pd
from scipy.stats import t

# Problem 1
x_mean = 3.8
y_mean = 2.1
x_num = 18
y_num = 25

Sp2 = 0.13
α = 0.05

# print(α)
Sxy = math.sqrt(Sp2/x_num + Sp2/y_num)
tcritical = t.ppf(.95, (x_num + y_num) - 2) # One tailed t-test
# print(tcritical)
tstat = (x_mean - y_mean)/Sxy
# print(tstat)

# Problem 2
x1_mean = 12
x2_mean = 8

n1 = 52
n2 = 57

Sp2_2 = 5.1

# h0: μ1 - μ2 = 3
# hA: μ1 - μ2 ≠ 3
α = 0.05
Sx1x2 = math.sqrt(Sp2_2/n1 + Sp2_2/n2)
# Careful: we're comparing against 3, not 0 as the
# difference between means
tstat = (x1_mean - x2_mean - 3)/Sx1x2 
print(tstat)
tcritical2 = t.ppf(.975, (n1 + n2) - 2) # Two tailed t-test
print(tcritical2)