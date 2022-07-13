db.query(`
INSERT INTO
cart
VALUES
(${req.body.product_id}, ${req.headers.authorization}, 1)
`,
