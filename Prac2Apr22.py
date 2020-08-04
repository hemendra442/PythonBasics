"""
tuple = (1,2,3,4,4,44,[5,6,7,8],{5,6,7,8})
list = [1,2,3,4,4,44,[5,6,7,8],{5,6,7,8}]

#If count is more than 2, printing index only one time
for i in range(0,len(list)):
    print("Count & Index of: ",list[i],list.count(list[i]),list.index(list[i]))

indexpos =0
for i in range(0,len(list)):
    if list.count(list[i])>1 :
        indexpos = list.index(list[i])+1
    print(list.index(list[i],indexpos))

list2 = [x**2 for x in range(0,5)]
list3 = 2*list2
print(list2)
print(list3)
"""
#SETS

set = {(1,2,3),2,3,45}
print(len(set))

Weekdays = {"Mon","Tue","Wed","Thu","Fri"}
Weekend = {"Sat","Sun"}
Days = Weekdays|Weekend
print(Days)

for d in Days:
    print(d)

A = {1,9,8,7,6}
B = {1,2,8,3,6}
C = {1,6,5,7,6}

print(A|B|C)
print(A&B&C)
print(A|B&C)
print(A&B|C)# First AND Operation then OR operation
print(A-B)
print(A-B-C)

#Dictionaries
dict = {"Sun":1, "Mon":2, "Tue":3,"Wed":4, "Thu":5}
print(dict["Mon"])
for k,v in dict.items():
    print(k,v)
print(dict.items())
print(dict.keys())
print(dict.values())