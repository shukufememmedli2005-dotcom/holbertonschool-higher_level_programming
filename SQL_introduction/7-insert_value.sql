-- Insert a new row into the table first_table
-- id = 89, name = 'Best School'
-- Using INSERT IGNORE ensures that if a row with the same PRIMARY KEY exists, it won't be added again
INSERT IGNORE INTO first_table (id, name)
VALUES (89, 'Best School');
