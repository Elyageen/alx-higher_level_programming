-- Script to list all records of table second_table with a name value, ordered by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;