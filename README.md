# Online Retail Store

This project is an implementation of an online retail store where customers can browse and purchase various items. It provides a user-friendly interface for customers to interact with the store, create accounts, add items to their shopping carts, place orders, and more.

- Aviral Dawar - 2020040
- Soumya Aggarwal - 2020134
- Utkarsh Arora - 2020143
- Vansh Gandhi - 2020147

## Features

- User Registration: Customers can create new accounts by providing their email address and password.
- Product Listing: Customers can browse through a wide range of products available in the store. Each product is displayed with its name, price, and available stock.
- Product Categories: Products are organized into different categories, allowing customers to easily find items of interest.
- Shopping Cart: Customers can add products to their shopping carts and review the total cost before proceeding to checkout.
- Order Placement: Customers can place orders for the items in their shopping carts. Each order includes the selected products, quantity, and order date.
- Delivery Partners: Orders are assigned to delivery partners who are responsible for delivering the products to customers.
- Customer Ratings: Customers can rate products based on their satisfaction and provide feedback for other users.
- Customer Complaints: Customers can raise complaints regarding products or services, which are then addressed by the customer care team.
- Discounts and Coupons: Customers can apply discount coupons during the checkout process to avail special offers and discounts.
- Account Management: Customers can view and update their account details, including personal information and contact details.

## Technologies Used

The online retail store is built using the following technologies:

- Front-end: HTML, CSS, JavaScript
- Back-end: Python, Flask framework
- Database: MySQL

## Relational Schema

- Account(Account_id, email, password)
- Customer(Customer_id, Account_id, First Name, Last Name, House Number, Street, City, State, Country, Age, PhoneNumber, cart_cost)
- Product(Product_ID, Name, Price, Stock, Category_ID)
- Rating(Product_ID, Customer_id, Rating)
- Complaints(Product_ID, Customer_id, ComplaintText)
- Category(Category_ID, Name)
- Supplier(Supplier_ID, Account_id, First Name, Last Name, Age, PhoneNumber, House Number, Street, City, State, Country)
- Supplies(Supplier_ID, Product_ID)
- Orders(Customer_ID, DeliveryPartner_ID, Product_ID, Coupon_ID, Status, Quantity, Order Date)
- Delivery Partner(DeliveryPartner_ID, Account_id, First Name, Last Name, House Number, Street, City, State, Country, PhoneNumber)
- Cart(Product_id, customer_id, Quantity)
- Customer_Coupon(Coupon_ID, Customer_ID)
- Coupon(Coupon_ID, Coupon_text, Valid_upto, Pct_disc)

## Indexing

Indexes are special lookup tables that speed up data retrieval in a database. They are automatically created for primary key constraints. In our project, we have created additional indexes for the Rating and Complaints tables to improve performance when retrieving data based on product_id and customer_id.

## Procedures

Procedures are reusable blocks of code that perform specific tasks in the database. In our project, we have created the following procedures:

- `check_stock`: Checks if the quantity of a product exceeds the available stock.
- `reduce_stock`: Updates the stock quantity of a product after a purchase.
- `check_if_user_coupon`: Verifies if a specific coupon is associated with a customer.
- `use_up_coupon`: Removes the coupon from the customer's list after it has been used in an order.

## Triggers

Triggers are database objects that execute automatically in response to specific events, such as data modification. In our project, we have created the following triggers:

- `update_cost`: Updates the cart cost for a customer after a new item is added to their cart.
- `stock_limit_cart`: Checks the stock limit before inserting a new item into the cart.
- `coupon_exists_with_user`: Validates if a customer has a specific coupon before placing an order.
- `coupon_order`: Removes the coupon from the customer's list after it has been used in an order.

## Data Population

The data population process in this project involves generating random data and inserting it into various tables in the MySQL database. Python code is used to create functions for each table, which generate random values for different fields such as names, addresses, phone numbers, and dates. These functions are then called to populate the tables with the randomly generated data, ensuring a diverse and realistic dataset for testing and demonstration purposes.
