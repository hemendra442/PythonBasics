import numpy as np
import pandas as pd

a_list = ["a","b","c","d","e","f"]
b_list = list("ghijk")
ar = np.array(np.random.randint(0,50,10))
dic = { "A":0, "B":1, "C":3}
a_set = {"c","d","e","f"}
tup = (1,2,3,4,5)

series1 = pd.Series(a_list)
series2 = pd.Series(b_list)
series3 = pd.Series(ar)
series4 = pd.Series(dic)
# series5 = pd.Series(a_set) -- set is unordered.
series6 = pd.Series(tup)

print(series1)
print(series2)
print(series3)
print(series4)
# print(series5)
print(series6)