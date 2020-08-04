'''
#febonacci series without function
n = int(input("Enter the num of febonacci series"))
if(n>0):
    print(0)
if(n>1):
    print(1)
a=0
b=1
for i in range(2,n):
    c= a+b
    print(c)
    a,b = b,c
'''
#febonacci with defination

def fbs():
    a = 0
    b = 1
    if(n<0):
        print("Enter more than zero only")
    if n>0:
        print(a)
    if n>1:
        print(b)
    for i in range(2,n):
        c=a+b
        print(c)
        a,b = b,c

n = int(input("Enter the num of febonacci series"))
fbs()

