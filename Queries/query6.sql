select c.customer_id, d.phone_number
from customer as c, delivery_partner as d, orders as o
where o.customer_id=c.customer_id and o.delivery_partner_id=d.delivery_partner_id
;
