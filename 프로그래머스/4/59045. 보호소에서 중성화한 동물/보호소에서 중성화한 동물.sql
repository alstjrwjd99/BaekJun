SELECT i.ANIMAL_ID,i.ANIMAL_TYPE,i.NAME
from ANIMAL_INS i join ANIMAL_OUTS o using (ANIMAL_ID)
where i.SEX_UPON_INTAKE like 'Intact%'
and (o.SEX_UPON_OUTCOME like 'Neutered%' or o.SEX_UPON_OUTCOME like 'Spayed%')
order by 1