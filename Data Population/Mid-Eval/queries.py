import sqlite3

conn = sqlite3.connect("retail.db")
c = conn.cursor()

query0 ='''CREATE TABLE IF NOT EXIST Address(
address_id 
)'''



query1 = '''CREATE TABLE IF NOT EXIST Customer(
customer_id int PRIMARY KEY AUTO_INCREMENT,
first_name varchar(20),
last_name varchar(20),
email varchar(50),
phone_number varchar(15),
password varchar(25),
address_id int FOREIGN KEY REFERENCES Address(address_id)
)'''

query2 = '''CREATE TABLE IF NOT EXIST Product(
product_id int PRIMARY KEY AUTO_INCREMENT,
name varchar(40),
category_id int FOREIGN KEY REFERENCES Category(category_id),
supplier_id int FOREIGN KEY REFERENCES Supplier(supplier_id),
stock int,
price numeric(10,2),
rating int
)'''

query3 = '''CREATE TABLE IF NOT EXIST Orders(
order_id int PRIMARY KEY AUTO_INCREMENT,
customer_id int FOREIGN KEY PREFERENCES Customer(customer_id),
deliveryPartner_id int FOREIGN KEY PREFERENCES DeliveryPartner(deliveryPartner_id),
product_id int FOREIGN KEY PREFERENCES Product(product_id),
order_date int,
status varchar(30),
quantity int
)'''

query4 = '''CREATE TABLE IF NOT EXIST DeliveryPartner(
deliveryPartner_id int PRIMARY KEY AUTO_INCREMENT,
first_name varchar(20),
last_name varchar(20),
address_id int FOREIGN KEY REFERENCES Address(address_id),
phone_number varchar(15),
)'''

query5 = '''CREATE TABLE IF NOT EXIST Category(
category_id int PRIMARY KEY AUTO_INCREMENT,
name varchar(30)
)'''

query6 = '''CREATE TABLE IF NOT EXIST 












def create_the_tables():
    pass
