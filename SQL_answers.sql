-- Question 1
SELECT st.store_name,count(s.sale_id) as "Lobster Sales"
FROM store st
JOIN sales s ON s.store_id = st.store_id
WHERE s.ingredient_id = (SELECT ingredient_id FROM ingredient WHERE ingredient_name = 'Lobster Ravioli')
GROUP BY st.store_id
ORDER BY 2 desc;

-- Question 2
SELECT st.store_name,count(s.sale_id) as "Lobster Sales"
FROM store st
JOIN sales s ON s.store_id = st.store_id
WHERE s.ingredient_id = (SELECT ingredient_id FROM ingredient WHERE ingredient_name = 'Lobster Ravioli')
AND s.business_date BETWEEN "2021-04-01" and "2021-05-01"
GROUP BY st.store_id
ORDER BY 2 desc;

-- Question 3
SELECT st.store_name,count(s.sale_id) as "Lobster Sales"
FROM store st
JOIN sales s ON s.store_id = st.store_id
WHERE s.ingredient_id = (SELECT ingredient_id FROM ingredient WHERE ingredient_name = 'Lobster Ravioli')
AND s.business_date BETWEEN "2021-04-01" AND "2021-05-01"
GROUP BY st.store_id
HAVING count(s.sale_id) > 45
ORDER BY 2 desc;
