import numpy as np
import pandas as pd

ser1 = pd.Series(np.random.randint(0,10,7))
pos = [0,2,4]
print(ser1[pos])