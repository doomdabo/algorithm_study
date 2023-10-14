-- 코드를 입력하세요
SELECT u.user_id, u.nickname, sum(price) as total_sales
from USED_GOODS_BOARD as b join USED_GOODS_USER as u on b.WRITER_ID = u.user_id
where b.status = 'DONE'
group by u.user_id
having sum(price) >=700000
order by total_sales