-- List all cities with their state names in hbtn_0d_usa
-- Display: cities.id - cities.name - states.name (aliased as state_name)
-- Sort by cities.id in ascending order
SELECT 
    cities.id,
    cities.name,
    (SELECT states.name FROM states WHERE states.id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id ASC;
