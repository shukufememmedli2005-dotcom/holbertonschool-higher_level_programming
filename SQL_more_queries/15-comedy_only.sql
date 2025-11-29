-- List all shows with the genre Comedy
-- Display: tv_shows.title
-- Sort by tv_shows.title ASC
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id = (
    SELECT id
    FROM tv_genres
    WHERE name = 'Comedy'
)
ORDER BY tv_shows.title ASC;
