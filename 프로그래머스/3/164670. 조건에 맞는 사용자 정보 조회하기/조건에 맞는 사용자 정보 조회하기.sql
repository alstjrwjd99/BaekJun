-- 코드를 입력하세요
SELECT U.USER_ID, U.NICKNAME, concat(U.city," ",U.STREET_ADDRESS1," ",U.STREET_ADDRESS2) as 전체주소, concat(left(tlno,3), '-', mid(tlno,4,4), '-',mid(tlno,8,4)) as 전화번호
from USED_GOODS_BOARD B join USED_GOODS_USER U on B.writer_id = U.user_id
group by B.writer_id
having count(*) >= 3
order by 1 desc