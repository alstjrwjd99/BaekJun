SELECT A.id, B.fish_name, A.length
FROM fish_info A
JOIN fish_name_info B USING(fish_type)
JOIN (
    SELECT fish_type, MAX(length) AS max_length
    FROM fish_info
    GROUP BY fish_type
) AS max_fish
ON A.fish_type = max_fish.fish_type AND A.length = max_fish.max_length
ORDER BY A.id;