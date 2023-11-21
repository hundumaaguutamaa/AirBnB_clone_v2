--  prepares a MySQL server for the project. 
--  database hbnb_dev_db, new user, priveleges. 

CREATE DATABASE IF NOT EXIST hbnb_dev_db;
CREATE USER IF NOT EXIST 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
