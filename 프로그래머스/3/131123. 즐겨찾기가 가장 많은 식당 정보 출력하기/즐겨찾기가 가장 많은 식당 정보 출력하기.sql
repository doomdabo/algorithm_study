select food_type, rest_id, rest_name, favorites
from rest_info
where food_type in (
    select food_type
    from rest_info
    group by food_type
    having favorites = max(favorites)
)
order by food_type desc