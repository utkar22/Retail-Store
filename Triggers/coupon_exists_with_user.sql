create trigger coupon_exists_with_user
before insert
on Orders
for each row
call check_if_user_coupon(customer_id, coupon_id);
