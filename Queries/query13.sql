select CONCAT(delivery_partner.first_name," ",delivery_partner.last_name) as
delivery_partner_name, max(total_quantity) as pieces_delivered
from
(select delivery_partner_id, (sum(quantity)) as total_quantity
from orders
where status = "Delivered"
group by delivery_partner_id) as derived_table
left join delivery_partner
on derived_table.delivery_partner_id = delivery_partner.delivery_partner_id
;
