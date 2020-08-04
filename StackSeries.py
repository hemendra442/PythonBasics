import numpy as np
import pandas as pd

ser1 = pd.Series("abcdefgj")
ser2 = pd.Series(np.random.randint(0,10,5))

#horizantal
print(pd.concat[ser1,ser2], axis=0)

#Vertical
print(pd.concat[ser1,ser2], axis=1)