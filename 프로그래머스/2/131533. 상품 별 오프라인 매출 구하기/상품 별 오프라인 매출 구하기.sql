-- 코드를 입력하세요
SELECT p.product_code, SUM(p.price * o.sales_amount) sales
from PRODUCT p join OFFLINE_SALE o on p.PRODUCT_ID = o.PRODUCT_ID
GROUP BY p.product_id
ORDER BY sales DESC, p.product_code;