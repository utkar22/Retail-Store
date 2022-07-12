create trigger coupon_order
after insert
on Orders
for each row
call use_up_coupon(customer_id, coupon_id);
