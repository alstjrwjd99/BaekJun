select C.id
from ecoli_data C join (select B.id
from ecoli_data A join ecoli_data B on A.id = B.parent_id
where A.parent_id is null) D on C.parent_id = D.id
order by C.id