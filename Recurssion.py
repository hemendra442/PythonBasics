import sys
#print(sys.getrecursionlimit()) #Recursion limit
#Recursion example

n = int(input("Enter n for factorial"))
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result = fact(n)
print(result)

