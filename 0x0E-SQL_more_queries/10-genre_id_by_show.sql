-- List all shows in the database

SELECT ts.title, tsh.genre_id
FROM tv_shows ts
INNER JOIN tv_shows_genres tsh
	ON tsh.show_id = ts.id
ORDER BY ts.title, tsh.genre_id;
