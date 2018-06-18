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
# print(tstat)
tcritical2 = t.ppf(.975, (n1 + n2) - 2) # Two tailed t-test
# print(tcritical2)

# Problem 3
x_1_3_mean = 35.8
x_2_3_mean = 31.6
n_1_3 = 207
n_2_3 = 220
SS1_3 = 481 # "Sum of Squares"
SS2_3 = 322
# pooled variance = [(i - x_mean)**2 for i in sequence]
Sp2_3 = (SS1_3 + SS2_3)/(n_1_3 + n_2_3 - 2) 
# print(Sp2_3)
# 1.946100681162438
tcritical_3 = t.ppf(.995, (n_1_3 + n_2_3 - 2))
# print(tcritical_3)
# 2.587446721586483
Sx1_3x2_3 = math.sqrt((Sp2_3/n_1_3) + (Sp2_3/n_2_3))
tstat_3 = (x_1_3_mean - x_2_3_mean)/Sx1_3x2_3
# print(tstat_3)
# 31.555027166862935

# Problem 4
tcritical_4 = t.ppf(.95, 23)
# print(round(tcritical_4,3)) # OK
# 1.714

# Problem 5
# p-value = .003
# print(t.ppf(.003, 23))
# -3.0268119786325056

# Problem 6
# p-value = .28
# print(t.ppf(.28, 23))
# -0.5914313904329228

# Problem 7
x_5_1 = 9
x_5_2 = 8
SE_5 = 1.29
t_stat_5 = (9-8)/SE_5 # Correct, but why???

# Problem 9
# Compute the sum of squares for the following series
Sx_6 = pd.Series([2, -3, 5, 4, 7])
Sy_6 = pd.Series([10, 13, 15, 10])
SSx_6 = pd.Series([(x_6_i - Sx_6.mean())**2 for x_6_i in Sx_6]).sum()
SSy_6 = pd.Series([(y_6_i - Sy_6.mean())**2 for y_6_i in Sy_6]).sum()
# print(SSx_5)
# 58.0 # correct
# print(SSy_5)
# 18.0 # correct

# Problem 10
# Compute pooled variance
PV_6 = (SSx_6 + SSy_6)/((Sx_6.count()-1) + (Sy_6.count()-1))
# print(PV_6)
# 10.857142857142858 # Correct

# Problem 11
# Compute the standard error
SE_6 = math.sqrt(PV_6/Sx_6.count()+PV_6/Sy_6.count())
# print(SE_6)
# 2.210365192839022 # Correct

# Problem 12
# Compute the t-statistic
tstat_6 = (Sx_6.mean() - Sy_6.mean())/SE_6
# print(tstat_6)
# -4.071725355229776

# Problem 13
# Find two-tailed critical values at α = .01
# Do we accept or reject the null?
df_6 = (Sx_6.count()-1) + (Sy_6.count()-1)
tcritical_6 = t.ppf(.995, df_6)
# 3.4994832973505026

# We reject the null hypothesis since tstat_6 < -tcritical_6

# Problem 18
#  α = .05, two-tailed
# The means of two groups of 10
x_7_1 = 10
x_7_2 = 7

# Degrees of freedom = 10 + 10 - 2
df_7 = 18
tcritical_7 = t.ppf(.975, 18)

# Problem 19
# Calculate t-critical
# print(tcritical_7)
# 2.10092204024096

SE_7 = .94

tstat_7 = (10-7)/.94
print(tstat_7)
# 3.191489361702128

# Problem 21
# Cohen's d
# If pooled variance is 2.33
cohens_d_7 = (10-7)/2.33
# print(cohens_d_7)

# Problem 22
r2_7 = tstat_7**2/(tstat_7**2 + df_7)
print(r2_7)