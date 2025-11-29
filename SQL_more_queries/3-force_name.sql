-- Create the table force_name if it does not exist
-- id is an INT, name is a VARCHAR(256) and cannot be NULL
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
