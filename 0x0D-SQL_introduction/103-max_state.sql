-- Script to display the max temperature of each state ordered by State name

SELECT state, MAX(temperature) AS max_temp
FROM Temperatures
GROUP BY state
ORDER BY state;
