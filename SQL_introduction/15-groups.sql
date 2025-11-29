-- List the number of records per score in second_table
-- The result should display 'score' and 'number'
-- Sorted by number of records descending
SELECT score COUNT(*) AS numbers FROM second_table GROUP BY score ORDER BY number DESC;
