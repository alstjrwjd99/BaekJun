SELECT ROUND(SUM(
    CASE
        WHEN length IS NULL THEN 10
        ELSE length
    END
) / COUNT(id), 2) AS AVERAGE_LENGTH
FROM fish_info;