WITH A AS (SELECT HISTORY_ID, CAR_TYPE, DATEDIFF(END_DATE, START_DATE)+1 AS PERIODS, DAILY_FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
JOIN CAR_RENTAL_COMPANY_CAR C
ON H.CAR_ID = C.CAR_ID
WHERE C.CAR_TYPE = '트럭')

SELECT A.HISTORY_ID, ROUND((1-IF(ISNULL(D.DISCOUNT_RATE),0,D.DISCOUNT_RATE)/100)*DAILY_FEE*A.PERIODS ,0) AS FEE
FROM A
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN D
ON A.CAR_TYPE = D.CAR_TYPE AND
IF(A.PERIODS BETWEEN 7 AND 30,'7일 이상',
  IF(A.PERIODS BETWEEN 30 AND 90, '30일 이상',
  IF(A.PERIODS >= 90, '90일 이상','-'))) = DURATION_TYPE
ORDER BY FEE DESC, HISTORY_ID DESC