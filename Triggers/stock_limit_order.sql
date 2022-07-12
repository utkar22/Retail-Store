create trigger stock_limit_order
before insert
on Orders
for each row
call check_stock((select stock from product where product_id = new.product_id), new.quantity);
