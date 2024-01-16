-- Display top 3 cities during July and August

SELECT `city`, MAX(value) AS `avg_temp`
FROM `temperatures`
WHERE month IN (7, 8)
GROUP BY `city`
ORDER BY `avg_temp`
LIMIT 3;
