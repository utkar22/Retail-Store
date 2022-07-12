select category.name, avg(product.price)
from product
left join category
on product.category_id = category.category_id
group by category.name
;
