create table Product(
	product_id int PRIMARY KEY,
	name varchar(30) NOT NULL,
	stock int NOT NULL,
	price numeric(8,2) NOT NULL,
	category_id int ,

	FOREIGN KEY (category_id) REFERENCES Category(category_id)
	)
;
