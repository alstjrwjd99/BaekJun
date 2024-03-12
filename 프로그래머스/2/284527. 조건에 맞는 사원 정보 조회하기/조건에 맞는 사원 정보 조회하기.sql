select sum(c.score) score, b.EMP_NO, b.EMP_NAME, b.position, b.email
from HR_EMPLOYEES b join HR_GRADE c on b.emp_no = c.emp_no
group by c.emp_no
order by 1 desc
limit 1
