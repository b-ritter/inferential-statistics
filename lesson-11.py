import math

import pandas as pd
from scipy.stats import t

food_prices = pd.read_csv('Food Prices - Lesson 11 - Sheet1.csv', skiprows=1, names=['Gettysburg', 'Wilma'])

# Restaurant example
# print(food_prices.describe())
g = food_prices['Gettysburg']
w = food_prices['Wilma']

SE = math.sqrt(g.var()/g.count() + w.var()/w.count())

# print(SE)
# 0.8531100847677227 🌯

m_g = g.mean() 
m_w = w.mean()

tstat_1 = (m_g - m_w)/SE
tstat_2 = (m_w - m_g)/SE

tcritical = t.ppf(.975, (g.count() + w.count() - 2))

# print(tcritical) 👍

# Acne medication example

x1 = 33.5
x2 = 31.2
n1 = 6

S1 = 8.89
S2 = 10.16
n2 = 5

def samp(s, n): return pow(s, 2)/n

tacne = (x1 - x2) / (math.sqrt(samp(S1, n1) + samp(S2, n2)))

# print(t)

tcritical2 = t.ppf(.975, (n1 + n2 - 2))

# print(tcritical2) # 👍

# SHOES

shoes_data = pd.read_csv('Shoes - Lesson 11 - Sheet1.csv')

# print(shoes_data.describe())
m = shoes_data['Pairs of shoes (males)']
f = shoes_data['Pairs of shoes (females)']
mM = m.mean()
mF = f.mean()
SM = 34.272438
SF = 31.360424

SE = math.sqrt(samp(SM, m.count()) + samp(SF, f.count()))

tshoes = (mF - mM)/SE
# print((mF - mM)/SE) # 👍

tcritical_shoes = t.ppf(.975, m.count() + f.count() - 2)

## Confidence Interval
# x +/- t * SE
# Use difference between independent groups as basis for comparison
# Use tcritical
dMF = mF - mM
CIshoes = (dMF - tcritical_shoes * SE, dMF + tcritical_shoes * SE) # 👍

# r-squared
# r-squared explains what percent of the difference is attributable to
# gender (in this case)
t_shoes_2 = math.pow(tshoes, 2)
r2 =  t_shoes_2/ (t_shoes_2 + (m.count() + f.count() - 2))
# print(r2)

# Pooled Variance
pv = pd.DataFrame({
  'x': pd.Series([5,6,1,-4]),
  'y': pd.Series([3,7,8]).fillna(0)
})

x_num = pv['x'].count()
y_num = pv['y'].count()
x_mean = pv['x'].mean()
y_mean = pv['y'].mean()
pv['xvar'] = pv['x'] - pv['x'].mean()
pv['xvar_sq'] = pv['xvar']**2
pv['yvar'] = pv['y'] - pv['y'].mean()
pv['yvar_sq'] = pv['yvar']**2

SSX = pv['xvar_sq'].sum()
SSY = pv['yvar_sq'].sum()
pooled_variance = (SSX + SSY) / (pv['x'].count() + pv['y'].count() - 2)
# print(pv.describe())
# print(pooled_variance)
SEnumbers = math.sqrt((
    pooled_variance / x_num
  ) + (
    pooled_variance / y_num
  ))

t_stat_numbers = (x_mean - y_mean)/SEnumbers

t_critical_numbers = t.ppf(.975, x_num + y_num - 2)