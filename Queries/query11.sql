select product.name, max(product.price), category.name
from product
left join category
on product.category_id = category.category_id
where price<(select max(price) from product)
;
