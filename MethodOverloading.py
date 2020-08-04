def method_overload(x=4,y=2,z=1):
    return x+y+z

print(method_overload(z=4,y=1,x=2))
res = method_overload(4,x=4,y=4)    #cannot change positions while assigning
print(res)