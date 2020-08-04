
class Stack:

    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    def size(self):
        print(self.items)
        return len(self.items)

stack1 = Stack()
stack1.push(2)
stack1.push(4)
stack1.push(20)
print("Before pop Size:",stack1.size())
stack1.pop()
print("After 1 pop Size:",stack1.size())