-- Write your query below
SELECT name from CUSTOMERS
WHERE id NOT IN (SELECT customer_id FROM orders);