select case 
        when month(DIFFERENTIATION_DATE) <= 3 then '1Q'
        when month(DIFFERENTIATION_DATE) <= 6 and month(DIFFERENTIATION_DATE) > 3 then '2Q'
        when month(DIFFERENTIATION_DATE) <= 9 and month(DIFFERENTIATION_DATE) > 6 then '3Q'
        when month(DIFFERENTIATION_DATE) <= 12 and month(DIFFERENTIATION_DATE) > 9 then '4Q'
    end as QUARTER, count(*) as ecoli_count
from ECOLI_DATA
group by QUARTER
order by 1