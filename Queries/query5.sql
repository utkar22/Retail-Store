select delivery_Partner.delivery_partner_id, (select count(*) from Orders
where orders.delivery_partner_id = delivery_partner.delivery_partner_id
and Orders.status <> "Delivered") as "Undelivered Orders"
from Delivery_Partner
;
