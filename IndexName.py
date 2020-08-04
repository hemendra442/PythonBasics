import numpy as np
import pandas as pd

ser1 = pd.Series(list("abcdefgh"))
ser2 = pd.Series(np.random.randint(0,10,8))


ser1.name = "IND"
print("ser 1:\n",ser1)

df= pd.concat([ser1,ser2],axis=1)

print(df)