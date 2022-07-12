create table Customer(
	customer_id int PRIMARY KEY,
	account_id int UNIQUE,
	first_name varchar(30) NOT NULL,
	last_name varchar(30),
	age int,
	phone_number varchar(15),
	house_number varchar(20),
	street varchar(40),
	city varchar(20),
	state varchar(20),
	country varchar(20),
	cart_cost numeric(8,2) DEFAULT 0,

	FOREIGN KEY (account_id) REFERENCES Account(account_id) ON DELETE CASCADE,
	CHECK (age >= 13)
	)
;
