SELECT ORDER_ID, PRODUCT_ID, date_format(OUT_DATE,'%Y-%m-%d'),
(
    CASE 
        WHEN OUT_DATE IS NULL THEN '출고미정'
        WHEN OUT_DATE <= '2022-05-01' THEN '출고완료'
        ELSE '출고대기'
    END
) AS 출고여부
FROM FOOD_ORDER
order by ORDER_ID