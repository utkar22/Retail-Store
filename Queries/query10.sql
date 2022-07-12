Select S.supplier_id, P.name, P.stock
From supplier as S, supplies as sup, products as P
where s.supplier_id=sup.supplier_id
and sup.product_id=P.product_id
and P.stock<5
;
