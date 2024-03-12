SELECT b.ANIMAL_ID,b.NAME
from ANIMAL_INS a right join ANIMAL_OUTS b
using (ANIMAL_ID)
where 1=1
and a.ANIMAL_ID is null
and b.ANIMAL_ID is not null
order by a.ANIMAL_ID