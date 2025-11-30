-- List all shows and their genres (NULL if no genre)

SELECT S.title, G.name
FROM tv_shows S
LEFT JOIN tv_show_genres SG ON S.id = SG.show_id
LEFT JOIN tv_genres G ON SG.genre_id = G.id
ORDER BY S.title ASC, G.name ASC;
