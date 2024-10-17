SELECT Date_format(sales_date, '%Y-%m-%d') SALES_DATE,
       product_id,
       user_id,
       sales_amount
FROM   online_sale
WHERE  sales_date LIKE '2022-03%'
UNION
SELECT Date_format(sales_date, '%Y-%m-%d') SALES_DATE,
       product_id,
       NULL,
       sales_amount
FROM   offline_sale
WHERE  sales_date LIKE '2022-03%'
ORDER  BY 1, 2, 3