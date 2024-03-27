-- Script to print the full description of table first_table

SELECT CONCAT('Table: ', table_name) AS 'Table', 
       CONCAT('Create Table: ', create_statement) AS 'Create Table'
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';
