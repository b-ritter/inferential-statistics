from itertools import combinations
import pprint

import pandas as pd
from scipy.stats import f

# Quiz 3
pp = pprint.PrettyPrinter()
# pp.pprint(list(combinations(['A', 'B', 'C', 'D'], 2)))
# [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
# In the context of doing t-tests on groups of 4 different samples

# Quiz 21
fdf = pd.DataFrame({
  "snapzi":   pd.Series([15, 12, 14, 11]),
  "irisa":    pd.Series([39, 45, 48, 60]),
  "lolamoon": pd.Series([65, 45, 32, 38])
  })

means = [
  fdf['snapzi'].mean(),
  fdf['irisa'].mean(),
  fdf['lolamoon'].mean()
]

# print(fdf.describe())
# print(sum([snapzi_mean, irisa_mean, lolamoon])/3)
# 35.333333333333336 # correct

grand_mean = fdf.mean().mean()
# 35.333333333333336 # correct, neat!

# SS = 4 * sum([(x_i - grand_mean)**2 for x_i in means])
# 3010.666666666667

# Another way to calculate it
SS_between = 4*fdf.mean().apply(lambda x: (x - grand_mean)**2).sum()
# 3010.666666666667
# print(SS_between)
SS_within = fdf.apply(lambda x: (x - x.mean())**2).sum().sum()
# 862.0 # correct!
# print(SS_within)

df_between = 2
df_within = 9

MS_between = SS_between/df_between
MS_within = SS_within/df_within
# print(MS_between, MS_within)
# 1505.3333333333335 95.77777777777777
# print(MS_between/MS_within)

# F-Critical for α = .05
print(f.ppf(.95, 2, 9)) # correct
# 4.25649472909375