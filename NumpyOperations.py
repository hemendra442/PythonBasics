import numpy as np

a= np.array([[1,2,3],[4,5,6],[7,8,9]])  #list inside a list
b= np.array([(1,2,3),(4,5,6),(7,8,9)])  #tuple inside a list
c= np.array({{1,2,3},{4,5,6},{7,8,9}})  #set inside a list
print(" A Size: ",a.size)
print(a[:,1])

print(" B Size: ",b.size)
print(b[:,1])

print(" C Size: ",c.size)
#print(c[:,1]) -- error

