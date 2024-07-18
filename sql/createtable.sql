CREATE TABLE advisor (
id INTEGER PRIMARY KEY AUTOINCREMENT,
consultant_email varchar(50)
consultant_password varchar(50)
consultant_fullname varchar(50)
consultant_preferences list (10)
consultant_biography varchar(300)
);
