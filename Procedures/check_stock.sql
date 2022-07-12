DELIMITER //
create procedure check_stock(IN quantity int, IN stock int)
BEGIN
if quantity > stock
then SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient Stock';
end if;
end//
DELIMITER ;
