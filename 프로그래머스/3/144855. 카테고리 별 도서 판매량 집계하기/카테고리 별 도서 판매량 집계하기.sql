-- 코드를 입력하세요
SELECT b.category, sum(sales)
from book b join book_sales bs on b.book_id = bs.book_id
where bs.sales_date like '2022-01%'
group by category
order by category
