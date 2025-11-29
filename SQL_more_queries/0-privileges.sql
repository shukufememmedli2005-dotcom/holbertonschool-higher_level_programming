-- Attempt to show privileges for user_0d_1 on localhost
-- Since the user does not exist, MySQL will return ERROR 1141
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Attempt to show privileges for user_0d_2 on localhost
-- Since the user does not exist, MySQL will return ERROR 1141
SHOW GRANTS FOR 'user_0d_2'@'localhost';
