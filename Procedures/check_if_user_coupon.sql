DELIMITER //
create procedure check_if_user_coupon(IN c1 int, IN c2 int)
BEGIN
if (select count(*) from customer_coupon where customer_id = c1 and coupon_id = 2) = 0 
then SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No such coupon';
endif//
end//
DELIMITER ;
