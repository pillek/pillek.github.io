CREATE TABLE customer
customer_id int(30) PRIMARY KEY
customer_fullname varchar(50)
customer_username varchar(50)
customer_password varchar(50)

CREATE TABLE consultant
consultant_id int(30) PRIMARY KEY
consultant_fullname varchar(50)
consultant_email varchar(50)
consultant_password varchar(50)
consultant_preferences list (10)
consultant_biography varchar(300)