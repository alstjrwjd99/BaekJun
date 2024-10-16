select id,email,first_name, last_name
from DEVELOPER_INFOS
where 'Python' in (skill_1,skill_2,skill_3)
order by 1