-- Create the database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Create the table states if it does not exist
-- id is an INT, primary key, auto-incremented, and cannot be NULL
-- name is a VARCHAR(256) and cannot be NULL
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
