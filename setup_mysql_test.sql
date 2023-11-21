-- script that prepares a MySQL server for the project. 

-- Create the database hbnb_test_db if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user if it doesn't exist in the hbnb_test_db database.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the  hbnb_test_db database to the user.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema hbnb_test_db to the user.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
