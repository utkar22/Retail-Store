req.headers.authorization && db.query(`
INSERT INTO
rating
(product_id, customer_id, rating)
VALUES
(${req.body.product_id}, ${req.headers.authorization},
${req.body.rating})
ON DUPLICATE KEY UPDATE
rating=${req.body.rating}
