select Product.name, Product.stock, Customer.email
from Product, Customer, Orders
where Customer.customer_id = Orders.customer_id and Product.product_id = Orders.product_id
and Product.stock < 8
;
