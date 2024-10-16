SELECT distinct (cart_id)
from CART_PRODUCTS
where (cart_id, 'Milk') in (select cart_id, name from cart_products group by cart_id) and (cart_id, 'Yogurt') in (select cart_id, name from cart_products group by cart_id)
order by cart_id