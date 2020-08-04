class Node:

    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.value),
        printInorder(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

printInorder(root)