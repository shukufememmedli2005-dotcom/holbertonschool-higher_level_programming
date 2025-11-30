-- List all genres with the number of shows linked

SELECT G.name AS genre, COUNT(SG.show_id) AS number_of_shows
FROM tv_genres G
JOIN tv_show_genres SG ON G.id = SG.genre_id
GROUP BY G.name
ORDER BY number_of_shows DESC;
