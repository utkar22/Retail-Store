db.query(`
DELETE FROM
rating
WHERE
product_id=${req.body.product_id} AND
customer_id=${req.headers.authorization}
`,
