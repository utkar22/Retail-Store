db.query(`
DELETE FROM
cart
WHERE
customer_id=${req.headers.authorization} AND
product_id=${req.params.product_id}
`,
