select count(*) as FISH_COUNT, max(length) MAX_LENGTH, fish_type
from fish_info
group by fish_type
having avg(coalesce(length,10)) >= 33
order by fish_type