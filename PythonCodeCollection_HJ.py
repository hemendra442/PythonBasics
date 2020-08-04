import numpy as np

#Vector Addition
vectorA = [2,5,8,10,25]
vectorb = [12,55,18,20,75]
addAB =[]
for i in range(0,len(vectorA)):
    for j in range(0,len(vectorb)):
        if(i==j):
            addAB.append(vectorA[i]+vectorb[j])

print("Vector Addition addAB: \n",addAB)


#Vector Scalar Multiplication

mul =[]
for a in range(0,len(vectorA)):
    mul.append(vectorA[a]*5)
print("Vector-Scalar Multiplication: \n",mul)

#List of List
lil = [[1,2,3],[4,5,6,7],[7,8,9]]
c= lil.copy()

for m in range(0,len(lil)):
    for n in range(0,len(lil[m])):
        c[m][n] = 2*lil[m][n]
print("Vector2D-Scalar Multiplication: \n",c)

#Dot Product of 1D list
vectorA = [2,5,8,10,25]
vectorb = [12,55,18,20,75]
dp=0
for b in range(0,len(vectorA)):
    dp=dp+vectorA[b]*vectorb[b]
print("1D Dot Product: \n",dp)

#Dot Product of 2D list
v1= [[1,2,3],[4,5,6,7]]
v2= [[1,2,3],[4,5,6,7]]
dp=0
for i in range(0,len(v1)):
    for j in range(0,len(v1[i])):
        #print(v1[i][j], v2[i][j])
        dp = dp+v1[i][j]*v2[i][j]
print("2D Dot Product: \n",dp)

#vector matrix multiplication via dot products
    #Using Numpy
v1 = np.array([(1,2,3),(4,5,6)])
v2 = np.array([(2),(4),(8)])
print("vector matrix multiplication via dot products using Numpy: \n",np.dot(v1,v2))

#Lists
v1= [[1,2,3],[4,5,6]]
v2= [2,4,8]
dpv =[]

for i in range(0,len(v1)):
    for j in range(0,len(v1[i])):
        psum=0
        for k in range(0,len(v2)):
            psum+=v1[i][k]*v2[k]
    dpv.append(psum)
print("vector matrix multiplication via dot products using Lists: \n",dpv)

#vector matrix multiplication via linear functions
v1= [[1,2,3],[4,5,6]]
v2= [2,4,8]
dpv =[]

#Multiply v1 col elements with v2 element
for j in range(0,len(v1[0][:])):
    for i in range(0,len(v1)):
        v1[i][j]=v1[i][j]*v2[j]

#addition of multiplyed elements
for i in range(0,len(v1)):
    dpv.append(sum(v1[i]))

print("vector matrix multiplication via Linear functions: \n",dpv)



