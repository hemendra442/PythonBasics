class QuickSort:
    def quicksort(self,userList):

        if len(userList)<=1:
            print("length: ",len(userList))
            return userList
        else:
            pivot = userList.pop()

        greaterList=[]
        lowerList=[]

        for i in userList:
            if(i>pivot):
                greaterList.append(i)
            else:
                lowerList.append(i)
        return qs.quicksort(lowerList)+ [pivot] + qs.quicksort(greaterList)


n = int(input("Enter num of elements to be sorted using Quick Sort"))
userList =[]
for i in range(0,n):
    print("Enter element at: ",i)
    userList.append(int(input()))
print("UserList before Quick Sort:",userList)

#Calling quick sort function
qs = QuickSort()
qs.quicksort(userList)
#Print userList after Quick Sort
print("UserList after Quick Sort:",userList)