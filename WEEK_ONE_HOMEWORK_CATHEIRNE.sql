-- TASK 1 
-- 1.	Find the name and weight of each red part

-- USE PARTS;

-- SELECT PNAME, WEIGHT 
-- FROM PART
-- WHERE COLOUR = 'RED';

-- 2.	Find all unique supplier(s) name from London

-- SELECT distinct(SNAME) 
-- FROM supplier
-- WHERE CITY ='LONDON';

-- TASK 2
-- 1.	Find out how many sales (quantity) were recorded each week, per day (where available)

-- USE SHOP;

-- SELECT WEEK, DAY, COUNT(*) AS transactions 
-- FROM sales1
-- GROUP BY WEEK, DAY
-- ORDER BY WEEK, DAY;

-- 2.	Change the name of salesperson Inga to be Annette instead
-- USE SHOP;
-- SET SQL_SAFE_UPDATES = 0;

-- UPDATE sales1
-- SET SalesPerson = 'Annette'
-- WHERE SalesPerson= 'Inga';

-- SELECT SALESPERSON 
-- FROM SALES1;


-- 3.	Find out how many sales Annette logged
-- Note we’re looking for quantity here - e.g. if Annette did 6 sales, then output would be 6)

-- USE SHOP;

-- SELECT SALESPERSON, COUNT(*) AS transactions 
-- FROM SALES1
-- WHERE SALESPERSON = 'ANNETTE';


-- 4.	Find the total (sum) sales amount by each person by day

-- USE SHOP;

-- SELECT SALESPERSON, DAY, SUM(SALESAMOUNT) AS daily_sales 
-- FROM SALES1
-- GROUP BY SALESPERSON, DAY;   

-- 5.	How much (sum) each person sold for 

-- SELECT SALESPERSON, SUM(SALESAMOUNT) AS total_sales
-- FROM sales1
-- GROUP BY SalesPerson;

-- 6.	How much (sum) each person sold for, 
-- including the number of sales per person, their average, lowest and highest sale amounts

-- SELECT SALESPERSON, 
-- SUM(SALESAMOUNT) AS tot_sales, 
-- AVG(SALESAMOUNT) AS avg_sales, 
-- MIN(SALESAMOUNT) AS min_sales, 
-- MAX(SALESAMOUNT) AS max_sales 
-- FROM SALES1
-- GROUP BY SALESPERSON; 


-- 7.	Find the total  (sum) monetary sales amount achieved by each store

-- SELECT STORE, SUM(SALESAMOUNT) AS tot_store_sales 
-- FROM SALES1
-- GROUP BY STORE;

-- 8.	Find the number of sales by each person 
-- if they did less than 3 sales for the past period

-- SELECT SALESPERSON, COUNT(*) AS transactions
-- FROM SALES1
-- GROUP BY SALESPERSON
-- HAVING COUNT(*) < 3;

-- 9.	Find the total (sum) amount of sales by month where combined total is less than £100
-- USE SHOP;
-- SELECT MONTH,SUM(SALESAMOUNT) monthly_tot_sales 
-- FROM SALES1
-- GROUP BY MONTH
-- HAVING SUM(SALESAMOUNT) < 100;

-- TASK 3
-- USE PARTS;
-- 1.	Return the name and city of each project that’s not supplied by a London-based supplier

-- SELECT JNAME, CITY 
-- FROM PROJECT P
-- JOIN SUPPLY SP
-- 	ON P.J_ID = SP.J_ID
-- WHERE CITY != 'LONDON';




-- 2.	Return the supplier name, part name and project name for each case 
-- where not only does the supplier supply a project with a part, 
-- but also the supplier’s city, project city and part city are the same

-- USE PARTS;

-- SELECT SNAME, PNAME, JNAME
-- FROM SUPPLY SP
-- JOIN PROJECT P
-- 	ON P.J_ID = SP.J_ID
-- JOIN PART PA 
-- 	ON PA.P_ID = SP.P_ID
-- JOIN SUPPLIER S
-- 	ON S.S_ID = SP.S_ID
-- WHERE P.CITY = S.CITY = PA.CITY;







