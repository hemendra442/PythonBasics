number = int(input("Enter a number to verify prime or not"))

for i in range(2,number):
    if(number%i==0 and i!=number):
        print(number, "is not a prime number")
        break
else: print(number ,"is a prime number")
