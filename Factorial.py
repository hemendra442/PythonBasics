'''
n = int(input("Enter factorial for "))
fact =1
for i in range(0,n):
    fact = fact+fact*i

print(fact)

'''

# Using Function
n = int(input("Enter number for factorial "))

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

for i in range(1,n+1):
    print("Factorial of: ",i,fact(i))