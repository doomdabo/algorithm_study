-- 코드를 입력하세요
SELECT i.NAME, I.DATETIME
from animal_ins i left join animal_outs o on i.ANIMAL_ID = o.ANIMAL_ID 
WHERE O.ANIMAL_ID IS NULL
order by i.datetime
limit 3