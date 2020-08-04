"""
Steps to import numpy
 1. pip3 install numpy -- command line
 2. File --> Settings --> Project --> Project Intrepeter

 *** For any package installation we need to follow the same procedure.
"""
import numpy as np
"""
ar = np.array([2,3,5,9,8])
print("ar:",ar)
print("ar Size: ", ar.size)
print("ar Sum: ",ar.sum())

ar2 = np.array({1,2,3})
print("ar2:",ar2)
print("ar2 Size: ", ar2.size)
print("ar2 Sum: ",ar2.sum())

ar3 = np.array((1,2,3))
print("ar3:",ar3)
print("ar3 Size: ", ar3.size)
print("ar3 Sum: ",ar3.sum())

#ar2 = np.array({1,2,3},{4,5,6}) TypeError: data type not understood
#ar3 = np.array((1,2,3),(4,5,6))  TypeError: data type not understood
#ar2d = np.array([1,2,3],[4,5,6]) TypeError: data type not understood

ar2d = np.array([(1,2,3),(4,5,6)])
print("ar2D:",ar2d)
print("ar2D Size: ", ar2d.size)
print("ar2D Sum: ",ar2d.sum())
print("Dimensions: ",ar2d.ndim)

ar3d = np.array([(1,2,3),(4,5,6),(7,8,9)])

print("ar3D:",ar3d)
print("ar3D Size: ", ar3d.size)
print("ar3D Sum: ",ar3d.sum())
print("ar3d.dtype: ",ar3d.dtype)
print("ar3d.diagonal: ",ar3d.diagonal())
print("Max: ",ar3d.max())
print("Min: ",ar3d.min())
print("Mean", ar3d.mean())
print("Dimensions: ",ar3d.ndim)
print("Shape: ",ar3d.shape)


# >>>>>>>>> Reshape >>>>>>
ars = np.array([(1,2,3),(4,5,6),(7,8,9),(10,11,12)])
print(ars)
print(ars.reshape(3,4))
print(ars.reshape(6,2))
print(ars.reshape(2,6))
print(ars.reshape(1,12))
print(ars.reshape(12,1))


# >>>>> Slicing >>>>>>>
asl = np.array([(1,2,3),(4,5,6),(7,8,9),(10,11,12)])
print(asl[0:])
print(asl[1:])
print("one element :",asl[1,1])
print("one row :",asl[1,:])
print("Last element in each row:",asl[0:,2])
print("Last element in each row from second row:",asl[1:,2])

# Min, Max, Sum, axis functions
print("Sum axis=0 :",asl.sum(axis=0))
print("Sum axis=1 :",asl.sum(axis=1))
print("sqrt of asl: ",np.sqrt(asl))
print("square of asl: ",np.square(asl))
print("Standard Deviation: ",np.std(asl))
print("sum np: ",np.sum(asl))

"""
#OPeration on two matrices
a= np.array([(1,2,3),(4,5,6)])
b = np.array([(1,2,3),(4,5,6)])
print("a+b :",a+b)
print("a-b :",a-b)
print("a*b :", a*b)
print("a/b :",a/b)
print("a*2 :", a*2)
print("b+2 :",b+2)

# Stack two arrays
print(np.vstack((a,b)))
print(np.hstack((a,b)))
print(a.ravel()) #single row


# Special Numpy function - sin(), cos(), exp , log
