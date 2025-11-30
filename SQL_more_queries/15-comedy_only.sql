-- List all Comedy shows

SELECT S.title
FROM tv_shows S
JOIN tv_show_genres SG ON S.id = SG.show_id
JOIN tv_genres G ON SG.genre_id = G.id
WHERE G.name = 'Comedy'
ORDER BY S.title ASC;
