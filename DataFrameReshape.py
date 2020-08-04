import numpy as np
import pandas as pd

ser1 = pd.Series(np.random.randint(0,50,12))
print(pd.DataFrame(ser1.values.reshape(3,4)))