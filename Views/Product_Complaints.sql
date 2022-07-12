create view ProductComplaints as
select c.first_name as CustName , c.phone_number as PhoneNumber,
com.complaint_text as Complaint,p.name as ProductName
from Customer as c , Complaints as com , Product as p
where c.customer_id = com.customer_id and com.product_id = p.product_id
;
