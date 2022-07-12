CREATE USER IF NOT EXISTS 'supplier'@'localhost'
IDENTIFIED BY 'supplier';

GRANT INSERT
ON Supplies
TO 'supplier'@'localhost';

SHOW GRANTS FOR 'supplier'@'localhost';

REVOKE INSERT
ON Supplies
FROM 'supplier'@'localhost';

SHOW GRANTS FOR 'supplier'@'localhost';

DROP USER IF EXISTS 'supplier'@'localhost';
