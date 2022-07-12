select s.supplier_id, a.email, concat(s.first_name,' ',s.last_name) as supplier_name,
sum(p.price*o.quantity*c.pct_discount/100) as Income
from supplier as s, account as a, product as p, orders as o, supplies, coupon as c
where s.account_id = a.account_id
and s.supplier_id = supplies.supplier_id
and supplies.product_id = p.product_id
and p.product_id = o.product_id
and o.coupon_id = c.coupon_id
group by s.supplier_id
order by Income desc
;
