select distinct(CONCAT(c.first_name, ' ', c.last_name)) as customer_name,
c.phone_number,
CONCAT(c.house_number, ', ', c.street, ', ', c.city, ', ', c.state, ', ', c.country) as
Customer_Address,
product.name as Product_name, rating.rating
from supplier
left join (supplies
left join (product
left join (rating
left join customer as c
on c.customer_id = rating.customer_id)
on product.product_id = rating.product_id)
on supplies.product_id = product.product_id)
on supplier.supplier_id = supplies.supplier_id
where rating.rating < 3
and supplier.supplier_id = 1
;
