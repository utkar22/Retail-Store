db.query(
` INSERT INTO
customer
(
account_id,
first_name,
last_name,
age,
phone_number,
house_number,
street,
city,
state,
country
)
VALUES
(
${res2[0].account_id},
"${req.body.firstName}",
"${req.body.lastName}",
${req.body.age},
${req.body.phoneNumber},
${req.body.houseNumber},
"${req.body.street}",
"${req.body.city}",
"${req.body.state}",
"${req.body.country}"
)
`,
