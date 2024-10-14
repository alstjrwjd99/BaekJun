SELECT price as MAX_PRICE
from PRODUCT
where price = (select max(price) from PRODUCT)