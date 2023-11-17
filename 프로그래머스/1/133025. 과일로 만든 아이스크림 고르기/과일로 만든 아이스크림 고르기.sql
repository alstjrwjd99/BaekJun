-- 코드를 입력하세요
SELECT distinct FLAVOR   from FIRST_HALF
where TOTAL_ORDER > 3000 and flavor in (                                       
select FLAVOR from ICECREAM_INFO where INGREDIENT_TYPE like "fruit_based")
order by TOTAL_ORDER desc