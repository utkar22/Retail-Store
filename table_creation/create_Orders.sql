create table Orders(
	customer_id int NOT NULL,
	product_id int NOT NULL,
	delivery_partner_id int NOT NULL, 
	quantity int NOT NULL,
	order_date date NOT NULL,
	coupon_id int,
	status varchar(20) NOT NULL,

	FOREIGN KEY (customer_id) REFERENCES Customer(customer_id) ON DELETE CASCADE,
	FOREIGN KEY (product_id) REFERENCES Product(product_id) ON DELETE CASCADE,
	FOREIGN KEY (delivery_partner_id) REFERENCES Delivery_Partner(delivery_partner_id) ON DELETE CASCADE,
	FOREIGN KEY (coupon_id) REFERENCES Coupon(coupon_id) ON DELETE CASCADE,
	CHECK (quantity>0)
	)
;
