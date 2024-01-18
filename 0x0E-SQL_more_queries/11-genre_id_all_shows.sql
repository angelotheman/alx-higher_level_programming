-- Create genre for all

SELECT ts.title, tsh.genre_id
	FROM tv_shows ts
		LEFT JOIN tv_show_genres tsg
		ON ts.id = tsg.id
	ORDER BY ts.title, tsg.genre_id;
