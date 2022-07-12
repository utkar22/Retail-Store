select product.name,
(select count(*) from orders where orders.product_id = product.product_id) as
number_of_orders,
(select count(complaints.customer_id) from complaints where
complaints.product_id = product.product_id) as number_of_complaints,
(select avg(rating.rating) from rating where rating.customer_id =
product.product_id) as average_rating
from product
;
