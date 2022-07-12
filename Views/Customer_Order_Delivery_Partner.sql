create view_customer_order_delivery_partner as
select o.customer_id, p.name as ordered_product,
o.quantity as quantity, o.order_date as order_date,
o.status as status, a.email as delivery_partner_email,
CONCAT(dp.first_name,' ',dp.last_name) as
delivery_partner_name,
dp.phone_number as delivery_partner_phone_number
from product as p, orders as o, account as a,
delivery_partner as dp
where p.product_id = o.product_id
and o.delivery_partner_id = dp.delivery_partner_id
and dp.account_id = a.account_id
;
