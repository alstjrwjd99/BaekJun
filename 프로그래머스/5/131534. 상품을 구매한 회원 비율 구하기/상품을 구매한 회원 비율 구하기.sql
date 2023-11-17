-- 코드를 입력하세요
SELECT YEAR(sales_date) AS YEAR, MONTH(sales_date) AS MONTH, COUNT(DISTINCT O.USER_ID) AS PUCHASED_USERS,
ROUND( COUNT(DISTINCT u.USER_ID) / (SELECT COUNT(*)
                                    FROM USER_INFO
                                    WHERE YEAR(JOINED) = '2021'),1) AS PUCHASED_RATIO
from USER_INFO u join ONLINE_SALE o on u.USER_ID = o.USER_ID
where u.joined like "2021%"
GROUP BY YEAR(SALES_DATE), MONTH(SALES_DATE) 
ORDER BY YEAR, MONTH;