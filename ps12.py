import pandas as pd
from scipy.stats import f

# print(
#   f.ppf(.95, 3, 36),
#   f.ppf(.99, 3, 36)
#   )
# 2.86626555094018 4.377095620801177

# If the F-Ratio is 3.96, we reject
# the null hypothesis at α = .05 and 
# retain it at α = .01

# print(
#   f.ppf(.95, 3, 8),
#   f.ppf(.99, 3, 8)
#   )
# 4.06618055135116 7.590991947598852
# If the F-Ratio is 3.96, we retain
# the null hypothesis at both 
# α = .05 and α = .01

# Question 13
df = pd.DataFrame({
  'single_child': pd.Series([8, 7, 10, 6, 9]),
  'twin': pd.Series([4, 6, 7, 4, 9]),
  'triplet': pd.Series([4, 4, 7, 2, 3])
})
means = df.mean()
grand_mean = means.mean()
SS_between = df.shape[0]*df.mean().apply(lambda x: (x - grand_mean)**2).sum()
# print(SS_between)
# 40.0 # Correct. Remember, this is not the mean squares so we don't divide by df yet.

SS_within = SS_within = df.apply(lambda x: (x - x.mean())**2).sum().sum()
# print(SS_within)
# 42.0 # Correct

df_between = df.shape[1] - 1
df_within = df.size - df.shape[1]

# print(df_between, df_within)
# 2 12

MS_between = SS_between / df_between
MS_within = SS_within / df_within

# print(MS_between, MS_within)
# 20.0 3.5

F = MS_between / MS_within

# print(F)
# 5.714285714285714

f_critical = f.ppf(.95, 2, 12)
# print(f_critical)
# 3.8852938346523933

# Reject null

# Question 23
print(f.ppf(.95, 3, 25))
# 2.991240909549952
