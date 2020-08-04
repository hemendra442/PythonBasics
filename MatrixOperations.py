import numpy as np

M1 = np.matrix([(1,2,3),(4,5,6),(7,8,9)])
M2 = np.matrix([(1,2,3),(4,5,6),(7,8,9)])

print("Addition of M1,M2")
print(M1+M2)

print("Multiplication of M1,M2")
print(M1*M2)

a= np.matrix([(1,2,3),(4,5,6)])
b = np.matrix([(1,2,3),(4,5,6)])
#print("a*b :",a*b)  -- shapes (2,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)