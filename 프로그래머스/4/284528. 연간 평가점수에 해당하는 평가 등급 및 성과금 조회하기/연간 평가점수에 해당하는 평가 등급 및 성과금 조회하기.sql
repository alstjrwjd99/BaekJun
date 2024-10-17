select E.EMP_NO,E.EMP_NAME,(
    case
        when avg(G.score) >= 96 then 'S'
        when avg(G.score) >= 90 and avg(G.score) < 96 then 'A'
        when avg(G.score) >= 80 and avg(G.score) < 90 then 'B'
        else 'C'
    end 
) as grade , (
    case
        when avg(G.score) >= 96 then E.sal * 0.2
        when avg(G.score) >= 90 and avg(G.score) < 96 then E.sal * 0.15
        when avg(G.score) >= 80 and avg(G.score) < 90 then E.sal * 0.1
        else E.sal * 0
    end 
) as BONUS
from HR_DEPARTMENT D join HR_EMPLOYEES E using(dept_id) join HR_GRADE G using (emp_no)
group by E.EMP_NO
order by E.EMP_NO