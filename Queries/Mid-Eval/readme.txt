Query 1: Show all details about customers who live in Uttar Pradesh

select *
from Customer
where state = "Uttar Pradesh"

Query 2: Show the name of customers whose names start with 'A'

select first_name, last_name
from Customer
where first_name like 'A%'

Query 3: Lists email ID of customer ordering products whose stock is less than 8

select Product.name, Product.stock, Customer.email
from Product, Customer, Orders
where Customer.customer_id = Orders.customer_id and Product.product_id = Orders.product_id
and Product.stock < 8

Query 4: Lists customer between the ages of 18 and 65

select customer_id, first_name, last_name, age
from Customer
where age BETWEEN 18 and 65

Query 5: Lists number of undelivered orders for each delivery partner

select Delivery_Partner.delivery_partner_id, Delivery_Partner.first_name,
Delivery_Partner.last_name, (select count(*) from Orders 
where orders.delivery_partner_id = delivery_partner.delivery_partner_id
and Orders.status <> "Delivered") as "Undelivered Orders"
from Delivery_Partner

Query 6: Counts number of Senior Citizen customers

select count(*) as "Number of Senior Citizens"
from Customer
where age>65

Query 7: Products listed with their categories, that have the best reviews

select product.product_id, product.name, category.name,
(select avg(Rating.rating) from Rating 
where Rating.product_id = Product.product_id)
as "Average Rating"
from Product, Category
where 7<(select avg(Rating.rating) from Rating 
where Rating.product_id = Product.product_id)
and product.category_id = category.category_id

Query 8: Lists Phone Numbers of Customer, Delivery Partner and Supplier of orders involving Apples

select Customer.phone_number as "Customer Phone Number",
Supplier.phone_number as "Supplier Phone Number",
Delivery_Partner.phone_number as "Delivery Partner Phone Number"
from Customer, Supplier, Delivery_Partner, Product, Orders, Supplies
where Product.product_id = Orders.product_id
and Orders.delivery_partner_id = Delivery_Partner.delivery_partner_id
and Orders.customer_id = Customer.customer_id
and Product.product_id = Supplies.product_id
and Supplies.supplier_id = Supplier.supplier_id
and Product.name = "Apple"

Query 9: Lists a customer with ID 16's previous orders

select Customer.customer_id, Customer.first_name, Customer.last_name, Product.name, Orders.order_date
from Customer, Product, Orders
where Customer.customer_id = Orders.customer_id
and Product.product_id = Orders.product_id
and Customer.customer_id = 16

Query 10: Youngest Star Customer

select Customer.first_name, Customer.last_name, min(Customer.age) as "Youngest Star Customer Age"
from star_customer, customer
where star_customer.customer_id = customer.customer_id
