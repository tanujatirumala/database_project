CREATE SCHEMA Z1947594;

CREATE TABLE Z1947594.member (
name varchar(50),
address varchar(500),
PRIMARY KEY(name, address)
);

CREATE TABLE Z1947594.girl (
name varchar(50),
address varchar(500),
girl_rank varchar(20),
PRIMARY KEY(name, address),
FOREIGN KEY (name, address) REFERENCES Z1947594.member(name, address)
);

CREATE TABLE Z1947594.leader (
name varchar(50),
address varchar(500),
PRIMARY KEY(name, address),
FOREIGN KEY (name, address) REFERENCES Z1947594.member(name, address)
);

CREATE TABLE Z1947594.baker (
name varchar(50),
address varchar(500),
PRIMARY KEY(name)
);

CREATE TABLE Z1947594.council (
name varchar(50),
baker_name varchar(50),
PRIMARY KEY(name),
FOREIGN KEY (baker_name) REFERENCES Z1947594.baker(name)
);

CREATE TABLE Z1947594.service_unit (
name varchar(50),
number int NOT NULL,
council_name varchar(50),
PRIMARY KEY(number, council_name),
FOREIGN KEY (council_name) REFERENCES Z1947594.council(name)
);

CREATE TABLE Z1947594.troop (
number int NOT NULL,
council_name varchar(50),
service_unit_num int,
PRIMARY KEY(number, council_name, service_unit_num),
FOREIGN KEY (council_name, service_unit_num) REFERENCES Z1947594.service_unit(council_name,number)
);

CREATE TABLE Z1947594.member_troop (
name varchar(50),
address varchar(500),
troop_number int,
council_name varchar(50),
service_unit_num int,
PRIMARY KEY(name, address, troop_number, council_name, service_unit_num),
FOREIGN KEY (name, address) REFERENCES Z1947594.member(name, address),
FOREIGN KEY (troop_number, council_name, service_unit_num) REFERENCES Z1947594.troop(number, council_name, service_unit_num)
);

CREATE TABLE Z1947594.cookie (
name varchar(50),
PRIMARY KEY(name)
);

CREATE TABLE Z1947594.offers (
cookie_name varchar(50),
baker_name varchar(50),
PRIMARY KEY(cookie_name, baker_name),
FOREIGN KEY (cookie_name) REFERENCES Z1947594.cookie(name),
FOREIGN KEY (baker_name) REFERENCES Z1947594.baker(name)
);

CREATE TABLE Z1947594.sells_for (
council_name varchar(50),
cookie_name varchar(50),
price float,
PRIMARY KEY(council_name, cookie_name),
FOREIGN KEY (council_name) REFERENCES Z1947594.council(name),
FOREIGN KEY (cookie_name) REFERENCES Z1947594.cookie(name)
);

CREATE TABLE Z1947594.shop_sales (
cookie_name varchar(50),
troop_number int,
council_name varchar(50),
service_unit_num int,
sold_date date,
quantity int,
PRIMARY KEY(cookie_name, troop_number, council_name, service_unit_num, sold_date),
FOREIGN KEY (cookie_name) REFERENCES Z1947594.cookie(name),
FOREIGN KEY (troop_number, council_name, service_unit_num) REFERENCES Z1947594.troop(number, council_name, service_unit_num)
);



CREATE TABLE Z1947594.customer (
name varchar(50),
address varchar(500),
PRIMARY KEY(name, address)
);

CREATE TABLE Z1947594.individual_sales (
cookie_name varchar(50),
customer_name varchar(50),
customer_address varchar(500),
girl_name varchar(50),
girl_address varchar(500),
sold_date date,
quantity int,
PRIMARY KEY(cookie_name, customer_name, customer_address, girl_name,girl_address, sold_date),
FOREIGN KEY (cookie_name) REFERENCES Z1947594.cookie(name),
FOREIGN KEY (customer_name, customer_address) REFERENCES Z1947594.customer(name, address),
FOREIGN KEY (girl_name,girl_address) REFERENCES Z1947594.girl(name, address)
);





