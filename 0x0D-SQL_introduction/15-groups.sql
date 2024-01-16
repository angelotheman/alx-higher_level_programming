-- Aggregate the number of records
-- score, number of records as number

SELECT score, COUNT(score) AS `number`
FROM `second_table`
GROUP BY score
ORDER BY `number` DESC;
