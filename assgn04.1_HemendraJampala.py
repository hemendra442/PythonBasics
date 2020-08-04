#Big O Notation - O(N*logN)

class MergeSort:
    def mergesort(self,userList):

        if(len(userList)>1):
            m = len(userList)//2

        #Splitting the user List into 2 lists
            leftList = userList[:m]
            rightList =userList[m:]

        #Calling Recursive functions
            ms.mergesort(leftList)
            ms.mergesort(rightList)

            i=0
            j=0
            k=0
            while i<len(leftList) and j<len(rightList):
                if(leftList[i]<rightList[j]):
                    userList[k]=leftList[i]
                    i+=1
                else:
                    userList[k]=rightList[j]
                    j+=1
                k+=1

         #Storing remaining elements
            while i<len(leftList):
                userList[k] = leftList[i]
                i+=1
                k+=1
            while j<len(rightList):
                userList[k]= rightList[j]
                j+=1
                k+=1


n = int(input("Enter num of elements to be sorted using Merge Sort"))
userList =[]
for i in range(0,n):
    print("Enter element at: ",i)
    userList.append(int(input()))
print("UserList :",userList)

#Calling merge sort function
ms = MergeSort()
ms.mergesort(userList)

#Print userList after Merge Sort
print("UserList after Merge Sort:",userList)
