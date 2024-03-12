SELECT hour(DATETIME) as HOUR, count(*) as COUNT
from ANIMAL_OUTS
group by 1
having hour > 8 and hour < 20
order by 1