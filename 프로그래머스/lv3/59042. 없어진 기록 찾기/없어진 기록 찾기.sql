-- 코드를 입력하세요
SELECT o.ANIMAL_ID, o.name
from animal_ins i right join ANIMAL_OUTS o on i.animal_id = o.animal_id
where i.animal_id is null