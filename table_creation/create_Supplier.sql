create table Supplier(
	supplier_id int PRIMARY KEY,
	account_id int UNIQUE,
	first_name varchar(30) NOT NULL,
	last_name varchar(30),
	age int,
	phone_number varchar(15) NOT NULL,
	house_number varchar(20) NOT NULL,
	street varchar(40) NOT NULL,
	city varchar(20) NOT NULL,
	state varchar(20) NOT NULL,
	country varchar(20) NOT NULL,

	FOREIGN KEY (account_id) REFERENCES Account(account_id) ON DELETE CASCADE,
	CHECK (age>=18)
	)
;
