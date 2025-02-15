WITH max_colony AS (
    SELECT year(DIFFERENTIATION_DATE) AS YEAR, MAX(size_of_colony) AS max_size
    FROM ECOLI_DATA
    GROUP BY year(DIFFERENTIATION_DATE)
)
SELECT 
    year(ECOLI_DATA.DIFFERENTIATION_DATE) AS YEAR, 
    max_colony.max_size - ECOLI_DATA.size_of_colony AS YEAR_DEV,
    ECOLI_DATA.id
FROM ECOLI_DATA JOIN max_colony ON year(ECOLI_DATA.DIFFERENTIATION_DATE) = max_colony.YEAR
ORDER BY YEAR, 2