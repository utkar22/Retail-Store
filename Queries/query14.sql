select concat(customer.first_name,' ',customer.last_name) as customer_name,
count(*) as number_of_ratings,
avg(rating.rating) as average_rating, customer.cart_cost
from customer
left join rating
on customer.customer_id = rating.customer_id
group by customer.customer_id
having customer.cart_cost > 0
;
