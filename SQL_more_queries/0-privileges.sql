-- Check and create the users if they do not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Optional: grant some privileges if you want them to have any
-- GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

-- List privileges for user_0d_1 (only if exists)
SELECT CONCAT('Grants for user_0d_1@localhost:') AS info;
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- List privileges for user_0d_2 (only if exists)
SELECT CONCAT('Grants for user_0d_2@localhost:') AS info;
SHOW GRANTS FOR 'user_0d_2'@'localhost';
