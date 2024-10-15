SELECT category, price AS MAX_PRICE, product_name
FROM food_product AS fp
WHERE category IN ('과자', '국', '김치', '식용유')
AND price = (SELECT MAX(price) 
             FROM food_product 
             WHERE category = fp.category)
ORDER BY MAX_PRICE DESC;