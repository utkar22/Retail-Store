db.query(
` INSERT INTO
account
(email, password)
VALUES
("${req.body.email}", "${req.body.password}")
`,
