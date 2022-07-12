import names
import random
import mysql.connector

connection = mysql.connector.connect(host="localhost",user="root",passwd="moss" , database = "project")
cursor = connection.cursor()

country = ["India"]
house_number = [i for i in range(0,1000)]
street_list = ["Ambedkar Nagar" , "Sector 44" , "Sector 9" , "Sector 137" , "MG Road" , "Govindpuri" , "Harkesh Nagar"]
city_list = ["Delhi", "Mumbai", "Noida", "Aligarh", "Pune"]
state_list = {"Delhi": "Delhi", "Mumbai": "Maharashtra", "Noida": "Uttar Pradesh", "Aligarh": "Uttar Pradesh", "Pune": "Maharashtra"}

def add_to_table():
    for i in range(1,15):
        product_id = i

        name = input("Product name: ")
        stock = int(input("Stock: "))
        price = float(input("Price: "))

        category_id = int(input("Category Id: "))

        cursor.execute('''INSERT INTO Product (product_id, name, stock, price, category_id) VALUES(%s,%s,%s,%s,%s)''',(product_id, name, stock, price, category_id))

connection.commit()
