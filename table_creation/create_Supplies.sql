create table Supplies(
	supplier_id int NOT NULL,
	product_id int NOT NULL,

	FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id) ON DELETE CASCADE,
	FOREIGN KEY (product_id) REFERENCES Product(product_id) ON DELETE CASCADE
	)
;
