select Customer.customer_id, Customer.first_name, Customer.last_name, Product.name, Orders.order_date
from Customer, Product, Orders
where Customer.customer_id = Orders.customer_id
and Product.product_id = Orders.product_id
and Customer.customer_id = 16
;
