select product.name, complaints.complaint_text, rating.rating
from product
right join(
complaints
join rating
on complaints.product_id = rating.product_id and complaints.customer_id =
rating.customer_id
)
on product.product_id = complaints.product_id
;
