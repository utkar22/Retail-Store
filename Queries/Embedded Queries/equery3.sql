db.query(`
SELECT *
FROM
cart
INNER JOIN
product
ON
product.product_id=cart.product_id
AND cart.customer_id=${req.headers.authorization}
`,
