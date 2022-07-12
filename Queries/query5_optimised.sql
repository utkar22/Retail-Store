select delivery_partner.delivery_partner_id, count(*)
from delivery_partner
left join orders
on delivery_partner.delivery_partner_id = orders.delivery_partner_id
where status <> "Delivered"
group by delivery_partner_id
;
