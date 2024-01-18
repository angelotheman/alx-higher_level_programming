-- List all genres

SELECT 
	tg.name AS `genre`,
	Count(tsg.genre_id) AS `number_of_shows`
	FROM tv_genres tg
		JOIN tv_show_genres tsg
		ON tg.id = tsh.genre_id
	GROUP BY `genre`
	ORDER BY `number_of_shows` DESC;
