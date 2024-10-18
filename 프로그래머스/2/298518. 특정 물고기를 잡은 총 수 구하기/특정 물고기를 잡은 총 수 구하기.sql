select count(*) as FISH_COUNT
from fish_info join fish_name_info using(fish_type)
where fish_name in ('BASS','SNAPPER')