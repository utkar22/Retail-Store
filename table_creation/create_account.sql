create table Account(
	account_id int PRIMARY KEY,
	email varchar(30) NOT NULL UNIQUE,
	password varchar(30) NOT NULL
	)
;
