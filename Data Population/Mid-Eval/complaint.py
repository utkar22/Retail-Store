import names
import random
import mysql.connector

connection = mysql.connector.connect(host="localhost",user="root",passwd="moss" , database = "project")
cursor = connection.cursor()

country = ["India"]
house_number = [i for i in range(0,1000)]
street_list = ["Ambedkar Nagar" , "Sector 44" , "Sector 9" , "Sector 137" , "MG Road" , "Govindpuri" , "Harkesh Nagar"]
city_list = ["Delhi", "Mumbai", "Noida", "Aligarh", "Pune"]

s = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua,
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat, Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur, Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
officia deserunt mollit anim id est laborum'''
x = s.split(",")

for i in range(1,55):
    product_id=random.randint(1,14)
    customer_id = random.randint(1,109)
    complaint_text = random.choice(x)
    
    cursor.execute('''INSERT INTO Complaints (product_id,customer_id,complaint_text) VALUES(%s,%s,%s)''',(product_id,customer_id,complaint_text))

            

connection.commit()
