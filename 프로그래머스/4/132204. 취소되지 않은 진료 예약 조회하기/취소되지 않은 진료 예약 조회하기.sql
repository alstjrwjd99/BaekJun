SELECT a.APNT_NO,p.PT_NAME,p.PT_NO,d.MCDP_CD,d.DR_NAME,a.APNT_YMD
from PATIENT p,DOCTOR d,APPOINTMENT a
where p.PT_NO = a.PT_NO 
and d.DR_ID = a.MDDR_ID 
AND a.MCDP_CD = "CS"
and a.APNT_YMD like '2022-04-13%'
AND APNT_CNCL_YN = "N"
order by a.APNT_YMD
