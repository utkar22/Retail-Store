create trigger update_cost
after insert
on Cart
for each row
update customer
set cart_cost = (select * from (select customer.cart_cost from customer where customer.customer_id=new.customer_id) as cst) + (new.quantity * (select product.price from product where product.product_id = new.product_id))
where customer_id = new.customer_id
