import numpy as np
import pandas as pd

ser1 = pd.Series(np.random.randint(0,20,10))
print(ser1.where(lambda x:x%3==0).dropna())