from scipy.stats import f
from scipy.stats import f_oneway
import pandas as pd
import numpy as np
# Q1
# print(f.ppf(.95, 2, 30))

# Q2

# print(f.ppf(.95, 3, 15))

# Q12

# print(f.ppf(.95, 1, 30))
# 4.170876785766691

# Q13
# print(f.ppf(.95, 2, 50))
# 3.1826098520427744

# Q 17 - 26

ants_df = pd.DataFrame({
  'short': pd.Series([-8, -11, -17, -9, -10, -5]),
  'long': pd.Series([12, 9, 16, 8, 15]),
  'normal': pd.Series([.5, .0, -1., 1.5, .5,  -.1, 0])
})

# Q 18
# Grand Mean
# Concatenates all the columns and then takes the mean
GM = pd.concat([ants_df[column] for column in ants_df.columns]).mean()
# 0.07777777777777778 🏆

# Takes sum of the means of each column minus the grand mean squared
# multiplied by the length of each column
SS_between = ants_df.apply(lambda row: np.sum(row.count() * np.square(row.mean()-GM))).sum()
SS_within = ants_df.apply(lambda row: np.sum(np.square(row - row.mean()))).sum()
# print(SS_between)
# 1320.171111111111

df_between = 2
df_within = 15

MS_between = SS_between / df_between
MS_within = SS_within / df_within

# print(MS_between, MS_within)
# 660.0855555555555 8.898666666666665
F_ratio = 660.0855555555555 / 8.898666666666665

# print(F_ratio)
# 74.1780291679153

f_critical = f.ppf(.95, 2, 15)
# print(f_critical)
# 3.6823203436732412

η_squared = SS_within / (SS_between + SS_within)


# print(1 - η_squared)

# Q 25
kids_df = pd.DataFrame({
  'single': pd.Series([8, 7, 10, 6, 9]),
  'twin': pd.Series([4, 6, 7, 4, 9]),
  'triplet': pd.Series([4, 4, 7, 2, 3])
})

# print(kids_df.describe())
print(f_oneway(*[kids_df[kind].values for kind in kids_df.columns]))
# F_onewayResult(statistic=5.714285714285714, pvalue=0.018055629234348)
F = 5.714285714285714

# https://stats.stackexchange.com/questions/41861/calculating-eta-squared-from-f-and-df
df_1 = 2
df_2 = 12
eta_squared = (F*df_1) / (F*df_1 + df_2)
# print(eta_squared)
kidsSS_within = kids_df.apply(lambda row: np.sum(np.square(row - row.mean()))).sum()

# https://www2.stat.duke.edu/courses/Spring98/sta110c/qtable.html
q_star = 3.77

HSD = q_star * np.sqrt(kidsSS_within/df_2/len(kids_df.values))

# print(HSD)

# 3.154208300033465 🎯