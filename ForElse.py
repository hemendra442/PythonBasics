list =[10,25,12,19,88]

'''
for x in range(0,len(list)):
    if(list[x]%7==0):
        print(list[x])
    else: print(list[x],"is not divisible by 7")
'''
for x in range(0,len(list)):
    if(list[x]%7==0):
        print(list[x])
else: print("No element divisible by 7")