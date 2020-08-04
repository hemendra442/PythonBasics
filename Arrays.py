from array import *

vals = array('i',(1,2,3,-4,5,8,9))
print("Type: ",type(vals))
print("2nd index Value",vals[2])
print("vals: ",vals)
vals.reverse()
print("reverse vals: ",vals)

for i in range(0,len(vals)):
    print(vals[i])
#append -- adds element at the end
#insert -- adds element at given position
#remove --delete's first occurance of an element
#pop --delete element at given index
vals.append(2)
print("after append",vals)
vals.remove(2)
print(vals)
vals.append(9)
print(vals)
vals.remove(9)
print(vals)
vals.append(8)
print(vals)
vals.pop(5)
print(vals)