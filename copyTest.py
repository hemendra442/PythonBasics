import copy
#Shallow copy- appending will not effect newlist, but if we change oldlist which also in newlist, it will change
oldlist = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
newlist = oldlist.copy()
oldlist.append([4,4,4])
print(oldlist)
print(newlist)

print("Changing existing values will impact")

oldlist = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
newlist = oldlist.copy()
oldlist[1][1] = 5
print(oldlist)
print(newlist)

#Deep copy
print("Deep copy")
oldlist = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
newlist = copy.deepcopy(oldlist)
oldlist.append([4,4,4])
print(oldlist)
print("new list append: ",newlist)

oldlist = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
oldlist[1][1] = 5
print(oldlist)
print("new list update: ",newlist)
