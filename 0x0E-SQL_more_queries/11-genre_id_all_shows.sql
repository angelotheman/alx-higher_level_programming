-- Create genre for all

SELECT ts.title, tsh.genre_id
FROM tv_shows ts
RIGHT JOIN tv_show_genres tsg
	ON tsg.show_id = ts.id
ORDER BY ts.title, tsg.genre_id;
