class MovingAverage:

#Initializing variables
    def __init__(self,size):
        self.size=size
        self.nums=[]
        self.sum=0

#next method implementation
    def next(self,k):
        self.sum=0

        #push element
        self.nums.append(k)

        #pop using FIFO way if num of elements are more than given size
        if(len(self.nums)>self.size):
            self.nums.pop(0)

         #Calculate average
        for i in range(0,len(self.nums)):
            self.sum+=self.nums[i]
        return self.sum/len(self.nums)

#Creating object and calling sliding avg function next
m=MovingAverage(3)
print(m.next(1))
print(m.next(10))
print(m.next(3))
print(m.next(5))





