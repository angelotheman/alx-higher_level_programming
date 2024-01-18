-- List all shows without a genre Comedy

SELECT ts.title
	FROM ts_shows ts
	WHERE ts.id NOT IN (
		SELECT DISTINCT tsg.show_id
			FROM tv_show_genres tsg
			JOIN tv_genre tg
				ON tg.id = tsg.genre_id
			WHERE tg.name = 'Comedy'
		)
	ORDER BY ts.title;
