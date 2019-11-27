-- lists all genres from hbtn_0d_tvshows and displays the number of shows
SELECT tv_genres.name AS 'genre', COUNT(tv_genres.name) AS 'number_of_shows' FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
HAVING COUNT(tv_genres.name) > 0
ORDER BY COUNT(tv_genres.name) DESC;
