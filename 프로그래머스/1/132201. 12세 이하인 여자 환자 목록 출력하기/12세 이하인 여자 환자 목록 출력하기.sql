SELECT PT_NAME,PT_NO,GEND_CD,AGE,(
    case 
        when isnull(TLNO) then 'NONE'
    else TLNO
    end) as TLNO
from patient
where age <= 12 and gend_cd = 'W'
order by age desc, pt_name