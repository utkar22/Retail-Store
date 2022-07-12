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

status_list=["Delivered","Shipped","Out for Delivery","Packed"]

def date_gen():
    month = random.randint(1,2)
    date = random.randint(1,28)
    
    if date>9:
        s = f"2022-0{month}-{date}"
    else:
        s = f"2022-0{month}-0{date}"

    return s

for i in range(1,210):
    customer_id = random.randint(1,109)
    product_id=random.randint(1,14)
    delivery_partner_id = random.randint(1,14)
    quantity = random.randint(1,10)
    order_date = date_gen()
    status = random.choice(status_list)
    
    cursor.execute('''INSERT INTO orders(customer_id,product_id,delivery_partner_id,quantity,order_date,status)
VALUES(%s,%s,%s,%s,%s,%s)''',(customer_id,product_id,delivery_partner_id,quantity,order_date,status))

            

connection.commit()
