-- List all shows in the database

SELECT ts.title, tsh.genre_id
	FROM tv_shows ts, tv_shows_genres tsh
WHERE tsh.show_id = ts.id
ORDER BY ts.title, tsh.genre_id;
