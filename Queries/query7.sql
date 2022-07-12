select product.product_id, product.name, category.name,
(select avg(Rating.rating) from Rating
where Rating.product_id = Product.product_id)
as "Average Rating"
from Product, Category
where 7<(select avg(Rating.rating) from Rating
where Rating.product_id = Product.product_id)
and product.category_id = category.category_id
;
