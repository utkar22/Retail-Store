CREATE USER IF NOT EXISTS 'customer_care'@'localhost'
IDENTIFIED BY 'customer_care';

GRANT SELECT
ON Complaints
TO 'customer_care'@'localhost';

SHOW GRANTS FOR 'customer_care'@'localhost';

DROP USER IF EXISTS 'customer_care'@'localhost';
