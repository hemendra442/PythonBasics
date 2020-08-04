import numpy as np
import pandas as pd

ser1 = pd.Series([1,2,3,4,5,6])
print("Ser1 describe", pd.Series.describe(ser1))

ser2 = pd.Series(['a','b','c','d','e','f'])
ser3 = pd.Series(np.random.randint(0,10,6))
df = pd.concat([ser2,ser1,ser3], axis=1)
print(df)
print(df.describe())  #np.percentile gives same output as describe method except