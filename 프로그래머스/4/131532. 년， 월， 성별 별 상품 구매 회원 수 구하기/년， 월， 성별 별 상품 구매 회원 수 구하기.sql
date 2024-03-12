SELECT year(o.SALES_DATE) as YEAR,month(o.sales_date) as MONTH,u.GENDER,count(distinct u.user_id) as USERS
from USER_INFO u , ONLINE_SALE o 
where u.gender is not null
and u.user_id = o.user_id
group by 1,2,3
order by 1,2,3