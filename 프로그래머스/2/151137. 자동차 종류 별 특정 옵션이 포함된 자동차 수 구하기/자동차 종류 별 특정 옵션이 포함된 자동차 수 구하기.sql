SELECT C.car_type AS CAR_TYPE, count(C.car_type) AS CARS
FROM CAR_RENTAL_COMPANY_CAR C
where C.OPTIONS like '%통풍시트%' 
    or C.OPTIONS like '%열선시트%'
    or C.OPTIONS like '%가죽시트%' 
GROUP BY C.car_type
ORDER BY CAR_TYPE