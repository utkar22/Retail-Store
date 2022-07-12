create table Customer_Coupon(

	customer_id int NOT NULL,
	coupon_id int NOT NULL,

	FOREIGN KEY (customer_id) REFERENCES Customer(customer_id) ON DELETE CASCADE,
	FOREIGN KEY (coupon_id) REFERENCES Coupon(coupon_id) ON DELETE CASCADE
)
;
