create table Rating(
	product_id int NOT NULL,
	customer_id int NOT NULL,
	rating int NOT NULL,


	FOREIGN KEY (product_id) REFERENCES Product(product_id) ON DELETE CASCADE,
	FOREIGN KEY (customer_id) REFERENCES Customer(customer_id) ON DELETE CASCADE,
	CHECK (rating BETWEEN 1 and 11)
	)
;
