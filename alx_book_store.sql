CREATE DATABASE alx_book_store;

CREATE TABLE  AUTHORS(
	author_id INT Primary Key,
	author_name VARCHAR(215)
);

CREATE TABLE Customers(
	customer_id INT Primary Key,
	customer_name VARCHAR(215),
	email VARCHAR(215),
	address VARCHAR(50)
);

CREATE TABLE Orders(
	order_id INT PRIMARY KEY,
	customer_id INT,
	order_date DATE,
	FOREIGN KEY(customer_id) REFERENCES  Customers(customer_id)
);

CREATE TABLE Books(
	book_id INT Primary Key,
	title VARCHAR(130),
	author_id INT ,
	price INT,
	publication_date DATE,
	FOREIGN KEY(author_id) REFERENCES AUTHORS(author_id)
);

CREATE TABLE Order_Details(
	orderdetailid INT  Primary Key,
	order_id INT ,
	book_id INT,
	quantity INT,
	FOREIGN KEY(book_id) REFERENCES Books(book_id),
	FOREIGN KEY(order_id) REFERENCES Orders(order_id)
);
