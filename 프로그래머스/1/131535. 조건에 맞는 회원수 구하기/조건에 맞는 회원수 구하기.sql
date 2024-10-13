-- 코드를 입력하세요
SELECT count(user_id) as users
from user_info
where year(joined) = 2021 and 20 <= age and age <= 29