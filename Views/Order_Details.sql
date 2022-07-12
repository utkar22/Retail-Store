create view order_details as
select a1.email as Supplier_Email, CONCAT(s.first_name,' ',s.last_name) as
Supplier_Name,
s.phone_number as Supplier_Phone_Number, s.house_number as
Supplier_House_Number,
s.street as Supplier_Street, s.city as Supplier_City, s.state as Supplier_State,
s.country as Supplier_Country,
p.name as Product_Name, o.quantity as Product_Quantity,
(o.quantity*p.price*(100-cp.pct_discount)/100) as Final_Price,
a2.email as Customer_Email, CONCAT(c.first_name,' ',c.last_name) as
Customer_Name,
c.phone_number as Customer_Phone_Number, c.house_number as
Customer_House_Number, c.street as Customer_Street,
c.city as Customer_City, c.state as Customer_State, c.country as Customer_Country
from Account as a1, Supplier as s, Product as p, Orders as o, Coupon as cp, Account
as a2, Customer as c, supplies
where a1.account_id = s.account_id
and s.supplier_id = supplies.supplier_id
and supplies.product_id = p.product_id
and p.product_id = o.product_id
and cp.coupon_id = o.coupon_id
and c.customer_id = o.customer_id
and a2.account_id = c.account_id
and o.delivery_partner_id = {}
;
