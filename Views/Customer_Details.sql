create view Customer_Details as
select a.email as email_address, c.first_name as first_name, c.last_name as
last_name, c.age as age, c.cart_cost as cart_cost
from Account as a, Customer as c
where a.account_id = c.account_id
;
