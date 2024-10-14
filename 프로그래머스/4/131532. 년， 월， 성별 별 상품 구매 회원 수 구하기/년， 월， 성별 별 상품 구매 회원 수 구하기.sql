SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH, gender, count(distinct(A.user_id)) as users
from user_info A
join online_sale B using(user_id)
WHERE GENDER IS NOT NULL
group by 1,2,3
order by 1,2,3
