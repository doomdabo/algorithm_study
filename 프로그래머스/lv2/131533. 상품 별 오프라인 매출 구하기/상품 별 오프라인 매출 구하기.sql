-- 코드를 입력하세요
select PRODUCT_CODE, sum(price*SALES_AMOUNT) as SALES
from product p join offline_sale o on p.product_id = o.product_id
group by product_code 
order by sales desc, product_code