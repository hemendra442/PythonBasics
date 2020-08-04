from array import *
n = int(input("Enter size of the Array"))
inArr = array('i',[])
for i in range(0,n):
    j =int(input("Enter the element"))
    inArr.append(j)

print(inArr)

searchElement = int(input("Enter element for searching"))
'''
for i in range(0,len(inArr)):
    if(searchElement==inArr[i]):
        print(searchElement,"found at",i)
        break
'''

for i in inArr:
    if(i==searchElement):
        print(searchElement,"found")
        break
else: print(searchElement,"Not found")