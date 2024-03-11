SELECT CAR_ID,CAR_TYPE,	DAILY_FEE,OPTIONS from CAR_RENTAL_COMPANY_CAR
where 1=1 and options like '%네비게이션%'
order by 1 desc