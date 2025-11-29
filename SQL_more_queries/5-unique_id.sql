-- Create the table unique_id if it does not exist
-- id is an INT with default value 1 and must be UNIQUE
-- name is a VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
