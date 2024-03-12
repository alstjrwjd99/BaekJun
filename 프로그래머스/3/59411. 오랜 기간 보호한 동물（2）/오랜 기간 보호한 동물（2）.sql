-- 코드를 입력하세요
SELECT i.ANIMAL_ID,i.NAME
from ANIMAL_INS i join ANIMAL_OUTS o using (animal_id)
order by datediff(o.datetime, i.datetime) desc
limit 2