from functools import reduce
""""
#lamda function
add = lambda n:n+2
result = add(5)
print(result)

mul = lambda n:n*n
result = mul(5)
print(result)

divide  = lambda n:n/2
result = divide(5)   #you can pass only one element jn lambda function
print(result)
"""

#Map, Reduce, Filter

nums = [1,2,3,4,5]
odds = list(filter(lambda n:n%2!=0,nums)) #creates a list of elements for which a function returns true

sum = reduce(lambda a,b:a+b, nums) #Reduce function is for two argument data manuplations
print("Sum", sum)

div = reduce(lambda a,b:a/b, odds) #Reduce function is for two argument data manuplations
print("Div", div)

mul = list(map(lambda n:n*n,nums))
print("mul", mul)

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items)) #applies a function to all the items in an input_list.