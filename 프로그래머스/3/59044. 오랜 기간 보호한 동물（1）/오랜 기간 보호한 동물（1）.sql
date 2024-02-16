SELECT i.NAME, i.DATETIME
FROM ANIMAL_INS i
    LEFT OUTER JOIN ANIMAL_OUTS o on i.ANIMAL_ID = o.ANIMAL_ID
WHERE 1=1 
    and o.NAME is null
    and i.NAME is not null
ORDER BY i.DATETIME ASC
LIMIT 3