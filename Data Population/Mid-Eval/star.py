import names
import random
import mysql.connector

connection = mysql.connector.connect(host="localhost",user="root",passwd="moss" , database = "project")
cursor = connection.cursor()

x=1
while (x<79):
    x=random.randint(x,x+10)
    cursor.execute('''INSERT INTO Star_Customer VALUES(%s)''',(x,))

connection.commit()
