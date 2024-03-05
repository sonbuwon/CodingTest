select sum(price) as "TOTAL_PRICE"
from ITEM_INFO
where rarity = "LEGEND"
group by rarity