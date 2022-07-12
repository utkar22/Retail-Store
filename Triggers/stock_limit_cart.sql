create trigger stock_limit_cart
before insert
on Cart
for each row
call check_stock((select stock from product where product_id = new.product_id), new.quantity);
