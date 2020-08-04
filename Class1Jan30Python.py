# Call By Refference in List
a =[1,2,3]
b=a
a[1]=5
print(b)

#Operators
print(5/2)
print(5//2) #Removing decimal point
print(5+2)
print(5--2) #adding
print(5*2)
print(5**2) #exponent

#SubStrings
s = "Hello Python"
print(len(s))
print(s[2:])
print(s[::])
print(s[:5])
print(s[0:8:1])
print(s[0:8:2])
print(s[0:12:1])
print(s[0:-1:1])
print(s[0:-2:1])

#Loops
for x in range(0,3):
    print("We're on time %d"%x)


#Hello world --- assignment
s = "hello world"
l = len(s)+1
i=0
for i in range(0,l):
    print(s[0:i])