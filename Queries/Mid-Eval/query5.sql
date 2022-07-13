select Delivery_Partner.delivery_partner_id, Delivery_Partner.first_name,
Delivery_Partner.last_name, (select count(*) from Orders 
where orders.delivery_partner_id = delivery_partner.delivery_partner_id
and Orders.status <> "Delivered") as "Undelivered Orders"
from Delivery_Partner
;
