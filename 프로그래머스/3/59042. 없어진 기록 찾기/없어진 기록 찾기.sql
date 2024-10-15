-- 코드를 입력하세요
SELECT distinct(O.ANIMAL_ID),O.NAME
from animal_ins I , animal_outs O 
where O.animal_id not in (select animal_id from animal_ins)
order by 1,2