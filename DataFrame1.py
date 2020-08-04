# 03/26/2020 to 03/27/2020 line 1 to 42

import pandas as pd
import numpy as np

corona_dataframe = pd.read_csv("C:\\Users\\Hemendra\\Desktop\\COVID19.csv")
"""
print("Shape of Carona Data set rows/col: ",corona_dataframe.shape) # rows,cols
print("DataFrame Size: ",corona_dataframe.size) # rows*cols
print(corona_dataframe.dtypes) #data type of each column

#[RangeIndex(start=0, stop=17892, step=1), 
#Index(['Id', 'Province/State', 'Country/Region', 'Lat', 'Long', 'Date','ConfirmedCases', 'Fatalities']
print(corona_dataframe.axes) #gives both range index and index(col names)
print(corona_dataframe.index) #RangeIndex(start=0, stop=17892, step=1) row size

print(corona_dataframe.head()) #few rows from top
print(corona_dataframe.tail()) #few rows from bottom
print(corona_dataframe.head(2)) #num of rows to show from top
print(corona_dataframe.tail(1)) #num of rows to show from bottom

#shows only include data, you should use atleast either include or exclude
print(corona_dataframe.select_dtypes(exclude="object", include="float"))

print(corona_dataframe.count()) #gives non NaN values of rows or columns
print(corona_dataframe.count(axis="rows")) #num of NaNs in each column
print(corona_dataframe.count(axis="columns")) #num of NaNs in each row


#converting from data frame to other data types Numpy/dict/excel/json
#print(corona_dataframe.to_numpy())
#print(corona_dataframe.to_dict())
#cs = corona_dataframe.to_json()

cd = corona_dataframe.reset_index(drop="true")
print(cd.head(2))
"""

#I need to do few excel operations
print(corona_dataframe["Id"].max(axis=0))
print(corona_dataframe["ConfirmedCases"].max(axis=0))
print(corona_dataframe["ConfirmedCases"].ndim)
