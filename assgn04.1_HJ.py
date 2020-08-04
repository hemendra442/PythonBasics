def mergesort(userList):

        if(len(userList)>1):
            m = len(userList)//2

        #Splitting the user List into 2 lists
            leftList = userList[:m]
            rightList =userList[m:]
            print("LeftList",leftList)
            print("rightList", rightList)
        #Calling Recursive functions
            mergesort(leftList)
            mergesort(rightList)

            i=0
            j=0
            k=0
            while i<len(leftList) and j<len(rightList):
                if(leftList[i]<rightList[j]):
                    userList[k]=leftList[i]
                    i+=1
                    print("user List inside leftList",userList)
                else:
                    userList[k]=rightList[j]
                    j+=1
                    print("user List inside Right List", userList)
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
mergesort(userList)