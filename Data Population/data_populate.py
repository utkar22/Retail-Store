import mysql.connector
import random
import names

connection = mysql.connector.connect(host="localhost",user="root",passwd="moss" , database = "end_project")
cursor = connection.cursor()

country = ["India"]
house_number = [i for i in range(0,1000)]
street_list = ["Ambedkar Nagar" , "Sector 44" , "Sector 9" , "Sector 137" , "MG Road" , "Govindpuri" , "Harkesh Nagar"]
city_list = ["Delhi", "Mumbai", "Noida", "Aligarh", "Pune"]
state_list = {"Delhi": "Delhi", "Mumbai": "Maharashtra", "Noida": "Uttar Pradesh", "Aligarh": "Uttar Pradesh", "Pune": "Maharashtra"}


def gen_random_text():
    n = random.randint(4,12)
    s = ""
    for i in range(n):
        s+= chr(random.randint(97,97+25))
    return s

def gen_phone_number():
    s = ""

    for i in range(10):
        n = random.randint(0,9)
        s+=str(n)

    return s

def gen_address():
    house_number = random.randint(1,999)
    street = random.choice(street_list)
    city = random.choice(city_list)
    state = state_list[city]
    country = "India"

    return house_number, street, city, state, country

def gen_name():
    first_name = names.get_first_name()
    last_name = names.get_last_name()

    return first_name, last_name

def gen_date():
    s = f"2022-0{random.randint(5,9)}-{random.randint(0,2)}{random.randint(0,9)}"
    return s

def gen_order_date():
    s = f"2022-0{random.randint(2,4)}-{random.randint(0,2)}{random.randint(0,9)}"
    return s

def add_to_account_table():
    for i in range(1,170):
        account_id = i
        email = gen_random_text() + "@gmail.com"
        password = gen_random_text()

        cursor.execute('''INSERT INTO ACCOUNT VALUES(%s,%s,%s)''',(account_id, email, password))

def add_to_customer_table():
    for i in range(1,140):
        customer_id = i
        account_id = i
        first_name, last_name = gen_name()
        age = random.randint(13,85)
        phone_number = gen_phone_number()

        house_number, street, city, state, country = gen_address()
        cart_cost = 0

        cursor.execute('''INSERT INTO Customer VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(customer_id,account_id, first_name, last_name, age, phone_number, house_number, street, city, state, country, cart_cost))

def add_to_supplier_table():
    for i in range(1,11):
        supplier_id = i
        account_id = i+140

        first_name, last_name = gen_name()
        age = random.randint(18,85)
        phone_number = gen_phone_number()

        house_number, street, city, state, country = gen_address()

        cursor.execute('''INSERT INTO Supplier VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(supplier_id,account_id, first_name, last_name, age, phone_number, house_number, street, city, state, country))

def add_to_delivery_partner_table():
    for i in range(1,20):
        delivery_partner_id = i
        account_id = i+150

        first_name, last_name = gen_name()
        age = random.randint(18,85)
        phone_number = gen_phone_number()

        house_number, street, city, state, country = gen_address()

        cursor.execute('''INSERT INTO Delivery_Partner VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(delivery_partner_id,account_id, first_name, last_name, age, phone_number, house_number, street, city, state, country))

        
def add_to_category_table():
    category_list = ["Fruit","Vegetable","Juice","Dairy","Biscuit","Meat"]
    for i in range(len(category_list)):
        cursor.execute('''INSERT INTO Category VALUES(%s,%s)''',(i+1,category_list[i]))

def add_to_product_table():
    pl1 = ["Apple","Banana","Pear","Strawberry","Watermelon","Muskmelon","Grape","Kiwi"]
    pl2 = ["Potato","Cucumber","Kale","Lettuce"]
    pl3 = ["Apple Juice","Mango Juice","Strawberry Juice","Mixed Fruit Juice"]
    pl4 = ["Milk","Cheese","Curd","Greek Yogurt","Yogurt","Paneer"]
    pl5 = ["Oreo","Hide n Seek","Bourboun","Parle-G"]
    pl6 = ["Chicken","Pork","Lamb","Tuna"]

    p = 1

    for i in pl1:
        stock = random.randint(2,20)
        price = random.randint(20,100)
        cursor.execute('''INSERT INTO Product VALUES (%s,%s,%s,%s,%s)''',(p,i,stock,price,1))
        p+=1

    for i in pl2:
        stock = random.randint(2,20)
        price = random.randint(20,100)
        cursor.execute('''INSERT INTO Product VALUES (%s,%s,%s,%s,%s)''',(p,i,stock,price,2))
        p+=1

    for i in pl3:
        stock = random.randint(2,20)
        price = random.randint(30,50)
        cursor.execute('''INSERT INTO Product VALUES (%s,%s,%s,%s,%s)''',(p,i,stock,price,3))
        p+=1

    for i in pl4:
        stock = random.randint(2,20)
        price = random.randint(10,100)
        cursor.execute('''INSERT INTO Product VALUES (%s,%s,%s,%s,%s)''',(p,i,stock,price,4))
        p+=1

    for i in pl5:
        stock = random.randint(2,20)
        price = random.randint(20,40)
        cursor.execute('''INSERT INTO Product VALUES (%s,%s,%s,%s,%s)''',(p,i,stock,price,5))
        p+=1

    for i in pl6:
        stock = random.randint(2,20)
        price = random.randint(50,200)
        cursor.execute('''INSERT INTO Product VALUES (%s,%s,%s,%s,%s)''',(p,i,stock,price,6))
        p+=1


def add_to_supplies_table():
    for p in range(1,31):
        s = random.randint(1,10)
        cursor.execute('''INSERT INTO Supplies VALUES (%s,%s)''',(s,p))

def add_to_rating_table():
    done = []
    for i in range(400):
        p = random.randint(1,29)
        c = random.randint(1,139)
        r = random.randint(1,10)

        if (p,c) not in done:
            cursor.execute('''INSERT INTO Rating VALUES (%s,%s,%s)''',(p,c,r))
            x = (p,c)
            done.append(x)

def add_to_complaints_table():
    complaints = ["Bad","Acha nahi hain","Ganda","Very Bad","Broken","Bad Colour","Too small","Bad Picture","Me do not likey","supplier sent hitmen to my house"]

    done = []
    for i in range(300):
        p = random.randint(1,29)
        c = random.randint(1,139)
        complain = random.choice(complaints)

        if (p,c) not in done:
            cursor.execute('''INSERT INTO Complaints VALUES (%s,%s,%s)''',(p,c,complain))
            x = (p,c)
            done.append(x)
    
def add_to_coupon_table():
    text = ["SAVING10","BACHAT20","SUPER25","DHAMAAL30","DISCOUNT40","SAVING50","SAVE70"]
    discount = [10,20,25,30,40,50,70]

    for i in range(1,8):
        curr_text = text[i-1]
        curr_discount = discount[i-1]
        date = gen_date()

        cursor.execute('''INSERT INTO Coupon VALUES (%s,%s,%s,%s)''',(i,curr_text,date,curr_discount))

def add_to_customer_coupon_table():
    for i in range(500):
        cust = random.randint(1,139)
        coup = random.randint(1,7)
        
        cursor.execute('''INSERT INTO Customer_Coupon VALUES (%s,%s)''',(cust,coup))

def add_to_cart_table():
    for i in range(100):
        p = random.randint(1,29)
        c = random.randint(1,139)
        q = random.randint(1,7)

        try:
            cursor.execute('''INSERT INTO Cart VALUES (%s,%s,%s)''',(p,c,q))
        except:
            pass

def add_to_orders_table():
    status_list=["Delivered","Shipped","Out for Delivery","Packed","Processing"]
    
    for i in range(50):
        customer_id = random.randint(1,129)
        product_id = random.randint(1,30)
        delivery_partner_id = random.randint(1,19)
        quantity = random.randint(1,3)
        order_date = gen_order_date()
        coupon_id = random.randint(1,7)
        status = random.choice(status_list)

        try:
            cursor.execute('''INSERT INTO ORDERS VALUES (%s,%s,%s,%s,%s,%s,%s)''',(customer_id, product_id, delivery_partner_id, quantity, order_date, 0, status))
            print ("Done")
        except Exception as e:
            print (e)
        


def populate_data():
    add_to_account_table()
    add_to_customer_table()
    add_to_supplier_table()
    add_to_delivery_partner_table()
    add_to_category_table()
    add_to_product_table()
    add_to_supplies_table()
    add_to_rating_table()
    add_to_complaints_table()
    add_to_coupon_table()
    add_to_customer_coupon_table()
    add_to_cart_table()
    add_to_orders_table()
