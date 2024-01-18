-- List all shows in the database

SELECT ts.title, tsg.genre_id
	FROM tv_shows ts, tv_show_genres tsg
WHERE tsg.show_id = ts.id
ORDER BY ts.title, tsg.genre_id;
