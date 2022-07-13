select product.name as Product_Name,
concat(customer.first_name, ' ', customer.last_name)
as Customer_Name, rating.rating
from rating use index (ix1), product, customer
where rating.product_id = product.product_id
and customer.customer_id = rating.customer_id
order by rating.rating desc
;
