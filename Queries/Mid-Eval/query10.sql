select Customer.first_name, Customer.last_name, min(Customer.age) as "Youngest Star Customer Age"
from star_customer, customer
where star_customer.customer_id = customer.customer_id
;
