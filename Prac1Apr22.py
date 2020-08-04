'''
l = []
n = int(input("Enter num of Elements"))
for i in range(0,n):
    l.append(int(input("Enter Element")))
print("List : ",l)


lol = []
m = int(input("Enter num of Row Elements"))
n = int(input("Enter num of Column Elements"))

for i in range(0,m):
    row = []
    print("Enter ",i, "row elements")
    for j in range(0,n):
        row.append(int(input("")))
    lol.append(row)
print("List of Lists: ", lol)



#Print Aij element
lol = [[1, 2], [2, 3], [3, 4]]
lo = [1, 2, 2, 3, 3, 4]
m = len(lol)
n = len(lol[0])
print("m,n :", m, n)
i = int(input("Enter i value"))
j= int(input("Enter j value"))

print("Aij :",lo[(i-1)*n +j-1])


#Convert list to list of lists
list = [1,2,3,4,5,6,7,8]
lil=[]
m = int(input("Enter num of rows required"))
n = int(input("Enter num of columns required"))

for i in range(0,m):
    row = []
    for j in range(0,n):
        row.append(list[(i*n+j)])
    lil.append(row)
print(m,"X",n," list: ",lil)

'''

#Convert list of lists to list
lol = [[1, 2], [2, 3], [3, 4]]
list=[]
m = len(lol)
n = len(lol[0])

for i in range(0,m):
    for j in range(0,n):
        list.append(lol[i][j])
print("Formed List is: ",list)