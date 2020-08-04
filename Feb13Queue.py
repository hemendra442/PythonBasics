class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        print(self.items)
        return len(self.items)

q = Queue()
q.enqueue(20)
q.enqueue(40)
q.enqueue(2)
q.enqueue(30)
print("Before Dequeue: ",q.size())
q.dequeue()
print("After 1st Dequeue: ",q.size())
q.dequeue()
print("After 2nd Dequeue: ",q.size())
