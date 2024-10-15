SELECT B.book_id, A.author_name, date_format(B.published_date,'%Y-%m-%d')
FROM BOOK B
JOIN author A ON B.author_id = A.author_id 
WHERE B.category = '경제'
ORDER BY B.published_date;