-- List all genres by their rating

SELECT tg.name, SUM(tsr.rate) AS `rating`
	FROM tv_genres tg
		JOIN tv_show_genres tsg
			ON tg.id = tsg.show_id
		JOIN tv_shows ts
			ON ts.id = tsg.show_id
		JOIN tv_show_ratings tsr
			ON ts.id = tsr.show_id
	GROUP BY `tg.name`
	ORDER BY `rating` DESC;
