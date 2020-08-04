import numpy as np
import pandas as pd

a_list = list("abcdefghijklmnopqrstuvwxyz")
myarr = np.arange(26)

ser = pd.Series(dict(zip(a_list,myarr)))
#print(ser[:5])

"""
ser_df = pd.DataFrame(ser)
ser_df.reset_index() #Not sure, why its not working
print(ser_df[:5])

"""
ser_df = ser.to_frame().reset_index()
print(ser_df[:5])
