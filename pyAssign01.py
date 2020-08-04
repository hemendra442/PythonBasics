#Hello world --- assignment using For loop
s = "hello world"
r = len(s)+1
i=0
print("hello world using For loop")
for i in range(0,r):
    print(s[0:i])

#Hello world --- assignment using While loop
print('\nhello world using While loop')
i=0
while i<r:
    print(s[0:i])
    i+=1