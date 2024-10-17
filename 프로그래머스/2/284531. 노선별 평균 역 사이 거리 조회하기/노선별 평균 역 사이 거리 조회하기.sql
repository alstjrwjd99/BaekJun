select route, concat(round(sum(D_BETWEEN_DIST),1),'km') as TOTAL_DISTANCE, concat(round(avg(D_BETWEEN_DIST),2),'km') as AVERAGE_DISTANCE
from SUBWAY_DISTANCE
group by 1
order by SUM(D_BETWEEN_DIST) desc
