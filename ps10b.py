import pandas as pd
import math
import numpy as np
from scipy.stats import t

df = pd.DataFrame({
  "Pre-Test" : [8,7,6,9,10,5,7,11,8,7],
  "Post-Test": [5,6,4,6,5,3,2,9,4,4]
})

df["Difference"] = df["Post-Test"] - df["Pre-Test"]

print(df.describe())

# t-critical at α = .95
tcritical = t.ppf(.05, 9)

# Standard Error
# S of difference = 1.3333
# print(1.33333/math.sqrt(10))
SE = 0.4216359672632305

# t-statistic
tstat = -3/SE
# -7.115142523235162

# Cohen's d
# print(-3/1.333333)
# -2.2500005625001402

tcritical_ci = t.ppf(.975, 9)

MoE = tcritical_ci * SE

print(-3 + MoE, -3 - MoE)