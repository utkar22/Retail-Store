create view product_details as
select product.name as Product_Name, product.price as Price, category.name as
Product_Category
from product
inner join category
on product.category_id = category.category_id
;
