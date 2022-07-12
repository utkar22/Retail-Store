DELIMITER //
create procedure reduce_stock(IN quantity int, IN p_id int)
BEGIN
update product set stock = (select * from (select stock from product where product_id = p_id) as stck) - quantity;
end//
DELIMITER ;
