-- List all genres for the show Dexter

SELECT G.name
FROM tv_shows S
JOIN tv_show_genres SG ON S.id = SG.show_id
JOIN tv_genres G ON SG.genre_id = G.id
WHERE S.title = 'Dexter'
ORDER BY G.name ASC;
