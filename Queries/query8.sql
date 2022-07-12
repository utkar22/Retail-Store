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
;
