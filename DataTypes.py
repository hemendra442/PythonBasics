#Int
books = 20
print(type(books))

#String
books = "Books are books"
print(type(books))

#tuple - (elements)
books = ("AmericanBook1","AmericanBook2","AmericanBook3")
print(type(books))

#List - [elements]
books = ["AmericanBook1","AmericanBook2","AmericanBook3"]
print(type(books))

#set - {elements}
books = {"AmericanBook1","AmericanBook2","AmericanBook3"}
print(type(books))

#dictionary - {key - value}
books = {"book1":"AmericanBook1","book2":"AmericanBook2","book3":"AmericanBook3"}
print(type(books))

#dictionary - specify explicitly - dict(key = "value")
books = dict(book1="AmericanBook1",book2="AmericanBook2",book3="AmericanBook3")
print(type(books))

#dictionary-  each item as a pair
books = dict([(1,'1'),(2,'2'),(3,'3')])
print(type(books))
#boolean
books = True
print(type(books))

#bytes
books =bytes(5)
print(books)
print(type(books))

#Range
books = range(6)
print(books)
print(type(books))


#byteArray
books = bytearray(5)
print(books)
print(type(books))

#Memory view byte
books = memoryview(bytes(5))
print(books)
print(type(books))

#Memory View byteArray
books = memoryview(bytearray(5))
print(books)
print(type(books))