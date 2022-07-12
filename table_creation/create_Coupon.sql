create table Coupon(
	coupon_id int PRIMARY KEY,
	coupon_text varchar(20),
	valid_upto date,
	pct_discount int NOT NULL,

	CHECK (pct_discount BETWEEN 1 and 100)
	)
;
