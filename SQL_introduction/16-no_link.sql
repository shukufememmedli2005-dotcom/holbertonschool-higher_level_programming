-- List all records with a non-empty name
-- Display score first, then name
-- Ordered by score descending
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
