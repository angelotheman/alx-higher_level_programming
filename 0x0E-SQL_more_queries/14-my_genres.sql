-- List all genres of the show Dexter

SELECT tg.name
	FROM tv_genres tg
		JOIN tv_show_genres tsh
		ON tg.id = tsh.genre_id
		JOIN tv_shows ts
		ON ts.id = tsh.show_id
	WHERE ts.title = 'Dexter'
	ORDER BY tg.name;
