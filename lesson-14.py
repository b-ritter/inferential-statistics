from itertools import chain
import math

import pandas as pd
import numpy as np
from scipy.stats import f

food_a = np.array([2, 4, 3])

food_b = np.array([6, 5, 7])

food_c = np.array([8, 9, 10])

food_gm = np.array(food_a + food_b + food_c).mean()

# print(food_gm)
# for item in [('a',food_a), ('b',food_b), ('c',food_c)]:
#   print(f'{item[0]} mean is {np.array(item[1]).mean()}')

# a mean is 3.0
# b mean is 6.0
# c mean is 9.0

# 🐄 food

foods = {
  'a': food_a,
  'b': food_b,
  'c': food_c
}

for food, weights in zip(foods.keys(),foods.values()):
  print(f'{food} sum of squares within groups: {np.sum(np.square(weights - weights.mean()))}')

# a sum of squares: 2.0
# b sum of squares: 2.0
# c sum of squares: 2.0 

# Degrees of freedom between = 2
# Degrees of freedom within = 6
# print(f.ppf(.95, 2, 6))
# 5.143252849784718 🐲

# watch the tuple argument
food_values = np.concatenate((food_a, food_b, food_c))

# Problem 10
# print(
#   np.sum(np.square(food_values - 6))
#   )

# Problem 16
# Compute Cohen's d
# Group A - B
# print((3 - 6)/math.sqrt(1))

# η^2
# print(54/60)

# Problem 22
# ANOVA with different sample sizes

data = {
  'placebo': pd.Series([1.5, 1.3, 1.8, 1.6, 1.3]),
  'drug_1' : pd.Series([1.6, 1.7, 1.9, 1.2]),
  'drug_2' : pd.Series([2.0, 1.4, 1.5, 1.5, 1.8, 1.7, 1.4]),
  'drug_3' : pd.Series([2.9, 3.1, 2.8, 2.7])
}

# Item Means
# for a, b in data.items():
#   print(f'{a} mean: {b.mean()}')

# Grand mean
df = pd.DataFrame(data)
# print(df)
GM = pd.concat([df['placebo'], df['drug_1'], df['drug_2'], df['drug_3']]).mean()
# 1.8350000000000002 🍄

# Takes sum of the means of each column minus the grand mean squared
# multiplied by the length of each column
SS_between = df.apply(lambda row: np.sum(row.count() * np.square(row.mean()-GM))).sum()
# print(SS_between)

# print(df.count().sum())
SS_within = df.apply(lambda row: np.sum(np.square(row - row.mean()))).sum()
# print(SS_within)
# 0.8360714285714287 🐓

MS_between = SS_between / (df.shape[1] - 1)

MS_within = SS_within / (df.count().sum() - df.shape[1])

print(MS_between, MS_within)

print(f'F = {SS_between/SS_within}')

print(f'η^2 = {SS_between/(SS_between + SS_within)}')