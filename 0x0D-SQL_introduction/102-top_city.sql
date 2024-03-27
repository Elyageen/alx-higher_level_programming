-- Script to display the top 3 cities' temperatures during July and August ordered by temperature (descending)

SELECT city, AVG(temperature) AS avg_temp
FROM Temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
