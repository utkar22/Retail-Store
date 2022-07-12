import names
import random
import mysql.connector

connection = mysql.connector.connect(host="localhost",user="root",passwd="moss" , database = "project")
cursor = connection.cursor()

for i in range(1,206):
    product_id=random.randint(1,14)
    customer_id = random.randint(1,109)
    rating = random.randint(1,10)
    
    cursor.execute('''INSERT INTO Rating (product_id,customer_id,rating) VALUES(%s,%s,%s)''',(product_id,customer_id,rating))

connection.commit()
