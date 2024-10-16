select D.DEPT_ID,D.DEPT_NAME_EN,round(avg(E.SAL)) as AVG_SAL
from HR_DEPARTMENT D join HR_EMPLOYEES E using(dept_Id)
group by dept_id
order by avg_sal desc