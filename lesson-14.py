import numpy as np

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
  print(f'{food} sum of squares: {np.sum(np.square(weights - weights.mean()))}')