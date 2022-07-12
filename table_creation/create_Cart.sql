create table Cart(
	product_id int NOT NULL,
	customer_id int NOT NULL,
	quantity int NOT NULL,

	FOREIGN KEY (product_id) REFERENCES Product(product_id) ON DELETE CASCADE,
	FOREIGN KEY (customer_id) REFERENCES Customer(customer_id) ON DELETE CASCADE,
	CHECK (quantity>0)

)
;
