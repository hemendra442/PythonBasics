import numpy as np
import pandas as pd

ser1 = pd.Series(np.random.randint(1,50,10))
ser2 = pd.Series(np.random.randint(1,50,10))

matched = ser1[ser1.isin(ser2)]
diffs1 = ser1[~ser1.isin(ser2)]
diffs2 = ser2[~ser2.isin(ser1)]

print(ser1)
print(ser2)
print(matched)
print(diffs1)

sums12 = pd.Series(np.union1d(ser1,ser2))
sames12 = pd.Series(np.intersect1d(ser1,ser2))
print(" Items not common to both series/n",sums12[~sums12.isin(sames12)])

