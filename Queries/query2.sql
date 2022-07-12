select customer_id, product_id, delivery_partner_id, coupon_id, quantity,
min(order_date)
from orders
where status <> "Delivered"
;
