select count(*) as FISH_COUNT,B.FISH_NAME
from FISH_INFO A join FISH_NAME_INFO B using(FISH_TYPE)
group by B.FISH_NAME
order by 1 desc