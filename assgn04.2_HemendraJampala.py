#Big O Notation - O(N log N)

class QuickSort:

    def quick_sort(self,userlist):
        if len(userlist)<1:
            print(userlist)
            return userlist

        else:
            pivot = userlist.pop()
            #print("pivot", pivot)

            lowerlist =[]
            upperlist=[]

            for i in userlist:
                if i<pivot:
                    lowerlist.append(i)
                else:
                    upperlist.append(i)
            print("Upper List: ",upperlist)
            print("Lower List:", lowerlist)
            return qs.quick_sort(lowerlist)+[pivot]+qs.quick_sort(upperlist)


n = int(input("Enter num of elements to be sorted using Quick Sort"))
userlist =[]
for i in range(0,n):
    print("Enter element at: ",i)
    userlist.append(int(input()))
print("UserList before QuickSort:",userlist)
qs = QuickSort()
print("After qucik sort: ",qs.quick_sort(userlist))
