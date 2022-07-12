DELIMITER //
create procedure use_up_coupon(IN c1 int, IN c2 int)
BEGIN
delete from Customer_Coupon where customer_id = c1 and coupon_id = c2;
end//
DELIMITER ; 
