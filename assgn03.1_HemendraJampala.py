#Big O Notation
#O(N)+ O(N^2)
# Big O -- O(N) for taking input elements from one for loop
# Big O -- O(N^2) for utilizing 2 for loops

class Caltrans:
    def __init__(self):
        self.inputMatrix = []
        self.transposeMatrix=[]

    def transpose(self):
        m = int(input("Enter m value for mxn matrix: "))
        n = int(input("Enter n value for mxn matrix: "))

# Big O -- O(N) for taking input elements from one for loop
        for i in range(0,m*n):
            x = int(input("Enter value: "))
            self.inputMatrix.append(x)

        print("Input Matrix mXn Values: ",self.inputMatrix)

# Big O -- O(N^2) for utilizing 2 for loops
        for i in range(0,n):
            for j in range(0,m):
                self.transposeMatrix.append(self.inputMatrix[i+n*j])

        print("Transpose Matrix nXm values: ",self.transposeMatrix)

ct = Caltrans()
ct.transpose()
