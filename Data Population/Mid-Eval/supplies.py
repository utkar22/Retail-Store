import names
import random
import mysql.connector

connection = mysql.connector.connect(host="localhost",user="root",passwd="moss" , database = "project")
cursor = connection.cursor()

country = ["India"]
house_number = [i for i in range(0,1000)]
street_list = ["Ambedkar Nagar" , "Sector 44" , "Sector 9" , "Sector 137" , "MG Road" , "Govindpuri" , "Harkesh Nagar"]
city_list = ["Delhi", "Mumbai", "Noida", "Aligarh", "Pune"]

def add_to_table():
    for i in range(1,15):
        product_id = i

        n = random.randint(3,7)

        supp = []

        for j in range(n):
            supplier_id = random.randint(1,15)

            if supplier_id in supp:
                continue
            supp.append(supplier_id)

            cursor.execute('''INSERT INTO supplies (supplier_id, product_id) VALUES (%s,%s)''',(supplier_id,product_id))
            

connection.commit()
