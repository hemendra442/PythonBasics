import numpy as np
import pandas as pd

ser1  = pd.Series(np.arange(6))
ser2 = pd.Series(list("abcdef"))

sersdf = pd.DataFrame(ser2,ser1).reset_index()
print(sersdf)

print(">>>>>>>>>>>> Method 2 >>>>>>>>>>>> ")
#Method 2
#pandas dataframe with Dict
dicdf = pd.DataFrame({"Index":ser1, "Values":ser2})
print(dicdf)

print(">>>>>>>>>>>> Method 3 >>>>>>>>>>>> ")
#Method 3
#pandas dataframe with concat
ser3 = pd.Series(np.random.randint(0,10,6))
concatdf = pd.concat([ser1,ser2,ser3],axis=1)
print(concatdf)