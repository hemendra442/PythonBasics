import numpy as np
import pandas as pd

ser1 = pd.Series(np.random.randint(0,10,20))
print(ser1)

print(ser1.value_counts(ascending=True))
ser1[~ser1.isin(ser1.value_counts().index[:2])] = 'other'
print(ser1)