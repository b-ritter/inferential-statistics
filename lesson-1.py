import math
import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd

from pprint import PrettyPrinter

pp = PrettyPrinter()
klout_df = pd.read_csv('Klout scores (Lesson 7) - Sheet1.csv', header=None, names=["Scores"])

# Two subplots on same figure
# Sets the figure size in inches (width, height)
plt.figure(figsize=(5,8))
pp.pprint(fm.fontManager.ttflist)
# raise
# pp.pprint(plt.axvlinercParams.keys())
# raise
# prop = fm.FontProperties(fname='/Users/br440r/Library/Fonts/AkzidGroProReg.otf')
plt.rcParams['font.family'] = 'DINOT'
# plt.rcParams['font.style'] = 'normal'
# plt.rcParams['font.variant'] = 'normal'
# plt.rcParams['font.weight'] = 'normal'
# plt.suptitle('Klout Scores', fontproperties=prop, size=32)
plt.suptitle('Klout Scores', size=16)
ax = plt.subplot(211)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

klout = klout_df.hist(bins=16, ax=ax, grid=False)

samples = [np.random.choice(klout_df['Scores'], 35).mean() for i in range(20000)]

samples_df = pd.DataFrame({"Sample Means": samples})

samples_df.sort_values("Sample Means")

ax2 = plt.subplot(212)
ax2.spines["top"].set_visible(False)  
ax2.spines["right"].set_visible(False)  

klout_samples = samples_df.hist(bins=40, ax=ax2, grid=False)

plt.savefig('klout.png')