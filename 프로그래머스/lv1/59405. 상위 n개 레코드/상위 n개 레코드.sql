-- 코드를 입력하세요
SELECT Name
from animal_ins
where (datetime) in 
(select min(datetime)
from animal_ins)

