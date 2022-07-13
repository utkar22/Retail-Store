db.query(
` SELECT
customer_id
FROM
account
INNER JOIN
customer
ON
account.account_id=customer.account_id
AND password="${req.body.password}"
AND email="${req.body.email}"
`,
