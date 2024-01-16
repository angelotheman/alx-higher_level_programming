-- Max temperature of each state
-- Order by state name

SELECT `state`, MAX(value) AS `max_temp`
FROM `temperatures`
GROUP BY `state`;
