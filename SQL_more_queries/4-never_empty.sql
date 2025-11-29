-- Create the table id_not_null if it does not exist
-- id is an INT with a default value of 1
-- name is a VARCHAR(256)
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
