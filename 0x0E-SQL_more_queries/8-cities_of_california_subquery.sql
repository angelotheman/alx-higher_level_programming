-- Cities in california database hbtn_0d_usa

SELECT `id`, `name`
FROM `cities`
WHERE `state_id` = (
	SELECT `id`
	FROM `states`
	WHERE `name` = 'Carlifornia'
)
ORDER BY id;
