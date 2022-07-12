create table Complaints(
	product_id int NOT NULL,
	customer_id int NOT NULL,
	complaint_text text NOT NULL,


	FOREIGN KEY (product_id) REFERENCES Product(product_id) ON DELETE CASCADE,
	FOREIGN KEY (customer_id) REFERENCES Customer(customer_id) ON DELETE CASCADE
	)
;
