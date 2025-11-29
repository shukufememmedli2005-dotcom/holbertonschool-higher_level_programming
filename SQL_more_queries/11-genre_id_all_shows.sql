-- List all shows with their genre IDs
-- Display: tv_shows.title - tv_show_genres.genre_id
-- If a show has no genre, display NULL
-- Sort by tv_shows.title ASC and genre_id ASC
SELECT 
    tv_shows.title,
    tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY 
    tv_shows.title ASC,
    tv_show_genres.genre_id ASC;
