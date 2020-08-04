def validate(string):
    store=[]
    for i in range(0,len(string)):
        if(string[i]!='}' and string[i]!=')' and string[i]!=']'):
            store.append(string[i])
            continue

        # Stack should not be empty while closed paranthesis started
        if (len(store) == 0):
            return False

        pop = store.pop()
        if ((string[i] == '}' and pop != '{') or (string[i] == ')' and pop != '(') or (string[i] == '[' and pop == ']')):
            return False
        #If stack empty it should be verified all elements
        if(len(store)==0 and i==len(string)-1):
            return True


#string = input("Enter pranthesis for validation")
string="[{([{()}])}]{{"


string1="()"
string2="()[]{}"
string3="([)]"
string4="{[]}"
print("Given assignment example validation")
print(string1,validate(string1))
print(string2,validate(string2))
print(string3,validate(string3))
print(string4,validate(string4))

print("My example validation")
if(validate(string)):
    print("String: ",string,"true")
else:print("String: ",string,"false")






