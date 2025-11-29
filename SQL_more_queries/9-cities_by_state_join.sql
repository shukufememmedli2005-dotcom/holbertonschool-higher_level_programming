-- List all cities with their state names in hbtn_0d_usa
-- Display: cities.id - cities.name - states.name
-- Sort by cities.id in ascending order
SELECT 
    id,
    name,
    (SELECT name FROM states WHERE states.id = cities.state_id) AS state_name
FROM cities
ORDER BY id ASC;
