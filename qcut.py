import numpy as np
import pandas as pd

ser1 = pd.Series(np.random.randint(0,50,20))
print(pd.qcut(ser1,10))