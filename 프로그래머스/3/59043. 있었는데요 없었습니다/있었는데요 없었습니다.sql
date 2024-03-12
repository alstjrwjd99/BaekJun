-- 코드를 입력하세요
SELECT i.ANIMAL_ID,i.NAME
from ANIMAL_INS i join ANIMAL_OUTS o using(ANIMAL_ID)
where i.DATETIME > o.DATETIME
order by i.DATETIME