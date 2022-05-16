create database store_1;
use store_1;
create table product(product_id int primary key,product_name varchar(20),price int,quantity int);
call insert_product(101,'pencil',5,10);
call insert_product(102,'pen',0,15);
call insert_product(200,'phone',15000,2);
call insert_product(108,'book',50,5);
