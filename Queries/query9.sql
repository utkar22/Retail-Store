select s.supplier_id
from supplier as s,supplies as sup , product as p, category as c
where s.supplier_id=sup.supplier_id and sup.product_id=p.product_id and
p.category_id=c.category_id and c.name="fruits"
UNION
select s.supplier_id
from supplier as s,supplies as sup , product as p, category as c
where s.supplier_id=sup.supplier_id and sup.product_id=p.product_id and
p.category_id=c.category_id and c.name="vegetables"
;
