from mysql import *

mydb = mysql.connector.connect(host="localhost", user="root", password="Jh$97857")
mycursor = mydb.cursor()
mycursor.execute("show databases")
for db in mycursor:
    print(db)
