-- List all cities of California from the database hbtn_0d_usa
-- Use a subquery to get the state_id of California
-- Sort the results by cities.id in ascending order
SELECT *
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
