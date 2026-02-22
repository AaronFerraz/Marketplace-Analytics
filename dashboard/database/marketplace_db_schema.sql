CREATE DATABASE IF NOT EXISTS marketplace;

USE marketplace;

SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS orders;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE IF NOT EXISTS customers(
    id int auto_increment, 
    firstname varchar(30), 
    lastname varchar(30), 
    country varchar(100), 
    score int,
    primary key (id)
);


CREATE TABLE IF NOT EXISTS employees(
    id int auto_increment, 
    firstname varchar(30),
    lastname varchar(30), 
    departament varchar(50), 
    birthday date, 
    gender varchar(1), 
    salary decimal(10, 2), 
    managerID int,
    primary key(id),
    foreign key (managerID) references employees(id)
);


CREATE TABLE IF NOT EXISTS products(
    id int auto_increment, 
    productname varchar(200), 
    category varchar(60), 
    price decimal(10, 2),
    cost_price decimal(10, 2),
    brand varchar(100),
    primary key (id)
);


CREATE TABLE IF NOT EXISTS orders( 
    id int auto_increment, 
    product_id int, 
    customer_id int, 
    salesperson_id int, 
    orderdate date, 
    shipdate date, 
    orderstatus varchar(2000), 
    shipaddress varchar(200), 
    billaddress varchar(200), 
    quantity int, 
    sales DECIMAL(10, 2), 
    payment_method varchar(100),
    creationtime datetime,
    primary key (id),
    foreign key (product_id) references products(id),
    foreign key (customer_id) references customers(id),
    foreign key (salesperson_id) references employees(id)
);


