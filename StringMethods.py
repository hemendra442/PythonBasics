hello ='Hello Python i am learning'
helloString = "Hello Python, i am learning"
helloLine = """Hello Python, i am learning
Will you help me!!"""

print("Single quote: ",hello)
print("Double quote: ",hello)
print("Triple quote: ",hello)

print("String Methods")

#Capitilize- convert first string to Capital and remaining all strings to lower
hello = "hello Python, I am learning"
print(hello.capitalize()) # observe h,p,I in output

#Casefold - converts everything into lower case even it's a german letter
hello = "hELLo PYTHON, I am learning"
print(hello.casefold())

#center -- Will fill the string with given char if provided more than string length
hello = "hello Python"
print(hello.center(2,'a')) #given < string length
print(hello.center(20,'a')) # given > String length
print(hello.center(12,'a')) #given = string length

#count of a string from any index
hello = "hello python hello how are you python hello"
print("Count2: ",hello.count("python"))
print("Count3: ",hello.count("hello"))
print("Count4: ",hello.count("o"))
print("Count5: ",hello.count("o",13,len(hello)))

#Ends with gives True or False
print("Ends with:",hello.endswith("hello"))
print("Ends with:",hello.endswith("python"))

#expandtabs -- replace /t with spaces
hello = "hello\thow\tare\tyou\tpython"
print("Expand tabs: ",hello.expandtabs())

#find/Index - gives lowest index of find with optional start and end of the string
hello = "hello Python hello Python"
print("find:",hello.find("ell"))
print("Index: ",hello.index("ell"))
print("find with slicing: ",hello.find("Python",0,len(hello))) #case sensitive

#format
hello = "Hello Python says {0} times"
print("Format: ",hello.format(10))

#format mapping

#isalnum
isalnum = "1232321321"
isalnum1= "a1s2b3"
isalnum2 = 125
isalnum3 = "12$"
isalnum4 = "aabbcc"
print("isalnum: ",isalnum.isalnum())
print("isalnum1: ",isalnum1.isalnum())
#print("isalnum2: ",isalnum2.isalnum()) #'int' object has no attribute 'isalnum'
print("isalnum3: ",isalnum3.isalnum())
print("isalnum4: ",isalnum4.isalnum())

print("isalnumalpha: ",isalnum.isalpha())
print("isalnum1alpha: ",isalnum1.isalpha())
print("isalnum3alpha: ",isalnum3.isalpha())
print("isalnum4alpha: ",isalnum4.isalpha())










#index of substring - gives index of the string start
#print(hello.index("lo"));
