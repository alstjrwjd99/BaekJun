SELECT COUNT(*) AS FISH_COUNT, b.fish_name AS FISH_NAME
FROM fish_info a
JOIN fish_name_info b
USING(fish_type)
GROUP BY b.fish_name
ORDER BY 1 desc