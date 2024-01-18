-- Create genre for all

SELECT ts.title, tsg.genre_id
	FROM tv_shows ts
		LEFT JOIN tv_show_genres tsg
		ON ts.id = tsg.show_id
	WHERE tsg.show_id is NULL
	ORDER BY ts.title, tsg.genre_id;
